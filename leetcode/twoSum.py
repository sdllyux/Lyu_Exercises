"""
在哈希表中查找j的时候存在一个先后顺序，先进行查找，再往哈希表中
存入index和num，例如：循环到num_1时，num对应的num_2还没添加进字典中，
但进行后续的循环时，循环到num_2时，对用的num_1已经添加进了哈希表中，
所以此方法可以排除数组中同一个元素使用两边的可能性
"""
class Solution:
    def twoSum(self, nums, target):
        hashmap = {}
        for index, num in enumerate(nums):
            j = target - num
            if j in hashmap:
                return [hashmap[j], index]
            hashmap[num] = index
        return None
