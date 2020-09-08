class Solution(object):
    def lengthOfLongestSubstring(self, s):
        left = 0  # 滑动窗口左边界
        res = 0  # 滑动窗口右边界

        hashmap = {}  # 哈希表用来储存临时变量
        # 判断存在
        if not s:
            return 0
        # for循环开始，右边界逐渐往前移
        for right in range(len(s)):
            # 判断右边界值是否与哈希表中储存的临时变量相等，相等就意味着重复
            if s[right] in hashmap:
                # 发生重复后，指针跳到上一次循环的right值+1的位置
                left = max(hashmap[s[right]], left)
            # 哈希表储存了上一轮循环时右边界的索引值+1
            hashmap[s[right]] = right + 1
            res = max(res, right - left + 1)
        return res
