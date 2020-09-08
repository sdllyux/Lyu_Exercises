import math
class Solution:
    def ishuiwen(self, d: int):
        digit = str(d)
        if len(digit) > 1:
            for i in range(math.floor(len(digit) / 2)):
                if digit[i] != digit[-(i + 1)]:
                    return False
        return True

    def nexthuiwen(self, d: int) -> int:
        digit = str(d)
        if digit.count("9") == len(digit):
            digit += "0"
            digit = digit.replace("9", "0")
            s = list(digit)
            s[0] = s[-1] = "1"
            return int("".join(s))
        else:
            s = list(digit)
            index = math.ceil(len(s) / 2) - 1
            while index >= 0:
                if s[index] != "9":
                    s[index] = str(int(s[index]) + 1)
                    s[-(index + 1)] = s[index]
                    break
                else:
                    s[-(index + 1)] = s[index] = "0"
                    index -= 1
            return int("".join(s))

    def superpalindromesInRange(self, L: str, R: str) -> int:
        sum = 0
        
        lhs = math.ceil(math.sqrt(int(L)))
        rhs = math.floor((math.sqrt(int(R)))) + 1
        i = lhs
        while i < rhs:
            if self.ishuiwen(i):
                if self.ishuiwen(i * i):
                    sum += 1
                i = self.nexthuiwen(i)
            else:
                i += 1
        return sum