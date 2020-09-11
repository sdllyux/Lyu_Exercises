class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        import bisect
        arr = []
        left = 0
        res = []
        for right in range(len(nums)):
            # 向arr中有序插入nums[right]
            bisect.insort(arr, nums[right])
            while len(arr) > k:
                # arr.pop()移除列表元素
                # bisecr.bisect_left(arr, nums[left]) 
                # 该函数用于处理将会插入重复数值的情况，返回将会插入的位置
                # 此处即为返回nums[left]的位置索引
                #（因为right添加到了arr中，left遍历的值都已经被right插入进了arr）
                arr.pop(bisect.bisect_left(arr, nums[left]))
                left += 1
            if len(arr) == k:
                # 此方法代替判断奇偶
                res.append((arr[k // 2] + arr[(k - 1) // 2]) / 2.0)
        return res

