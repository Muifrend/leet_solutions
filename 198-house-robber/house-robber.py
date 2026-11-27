class Solution:
    def rob(self, nums: list[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        if n == 2:
            return max(nums)
        m = max(nums[0]+nums[2], nums[1])
        if n == 3:
            return m
        arr = [nums[0],nums[1], nums[0]+nums[2]]
        for i in range(3, n):
            arr.append(nums[i] + max(arr[i-2], arr[i-3]))
            
        return max(arr)


        