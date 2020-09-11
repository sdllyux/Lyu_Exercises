from typing import List


class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        res = []

        def dfs(n, k, index, temp):
            if n == 0 and k == 0:
                res.append(temp[:])
                return
            for i in range(index, 10):
                if n - i < 0 or k <= 0:
                    break
                temp.append(i)
                dfs(n - i, k - 1, i + 1, temp)
                temp.pop()
            return

        dfs(n, k, 1, [])
        return res


sl = Solution()
print(sl.combinationSum3(3, 13))
