class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """               
        if not s:
            return 0
        d = {}
        cur = 0
        max_len = 0
        for i in range(len(s)):
            print(d)
            if s[i] in d and d[s[i]] >= cur:
                cur = d[s[i]] + 1
            d[s[i]] = i
            max_len = max(max_len, i - cur + 1)
        
        return max_len

sl = Solution()
sl.lengthOfLongestSubstring("hello")