class Solution(object):
    def longestOnes(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        right, left, count = 0, 0, 0

        for right in range(len(A)):
            # 滑动窗口的右边界
            if A[right] == 0:
                count += 1
            # 记录0的个数，当count > k时，开始移动左边界
            if count > K:
                if A[left] == 0:
                    count -= 1
                # 左窗口往前移1，若此时最左边值为0，则count -1 ，窗口右滑
                left += 1
        # 经过最大值后，窗口依然在滑动，但此时窗口的大小不会再改变，故返回的窗口大小即为窗口最大时的值
        return right - left + 1
        