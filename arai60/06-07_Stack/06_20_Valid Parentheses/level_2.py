class Solution:
    def isValid(self, s: str) -> bool:
        symbols = ["dummy"]
        mapping = {")": "(", "]": "[", "}": "{"}
        for i_char in s:
            if i_char == "(" or i_char == "[" or i_char == "{":
                symbols.append(i_char)
            else:
                close_symbol = symbols.pop()
                if close_symbol == "dummy":
                    return False
                elif close_symbol != mapping[i_char]:
                    return False
        return symbols[-1] == "dummy"
