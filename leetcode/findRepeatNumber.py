class Solution:
    def findRepeatNumber(self, nums):
        
        hashmap = {}

        for i in nums:
            if nums[i] not in hashmap:
                hashmap[i] = 1
            else:
                return i
