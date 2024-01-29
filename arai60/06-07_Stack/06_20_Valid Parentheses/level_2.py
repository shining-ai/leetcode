class Solution:
    def isValid(self, s: str) -> bool:
        symbols = ["dummy"]
        mapping = {")": "(", "]": "[", "}": "{"}

        for i_s in s:
            if i_s == "(" or i_s == "[" or i_s == "{":
                symbols.append(i_s)
            else:
                temp = symbols.pop()
                if temp == "dummy":
                    return False
                elif temp != mapping[i_s]:
                    return False

        return symbols[-1] == "dummy"
