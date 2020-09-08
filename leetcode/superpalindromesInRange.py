# L: "92904622" R: "232747148"时
# 这种方法超时
import math
class Solution:
    def superpalindromesInRange(self, L: str, R: str) -> int:
        count = 0
        for i in range(int(L), int(R)+1):
            if str(i)[::-1] == str(i):
                if int(math.sqrt(i))**2 == i:
                    if str(int(math.sqrt(i))) == str(int(math.sqrt(i)))[::-1]:
                        count += 1
        return print(count)


# 测试用
sl = Solution()
sl.superpalindromesInRange('4','1000')