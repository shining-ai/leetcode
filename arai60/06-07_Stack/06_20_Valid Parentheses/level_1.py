def check_straight(s):
    symbols = ["dummy"]

    for i_s in s:
        if i_s == "(" or i_s == "[" or i_s == "{":
            symbols.append(i_s)
        else:
            temp = symbols.pop()
            if temp == "dummy":
                return False
            elif i_s == ")" and temp != "(":
                return False
            elif i_s == "]" and temp != "[":
                return False
            elif i_s == "}" and temp != "{":
                return False

    if len(symbols) == 1:
        return True
    else:
        return False


if __name__ == "__main__":
    s = "()[]{}"
