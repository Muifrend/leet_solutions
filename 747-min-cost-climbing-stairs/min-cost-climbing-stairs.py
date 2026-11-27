class Solution:
    def minCostClimbingStairs(self, cost: list[int]) -> int:
        arr = [cost[0], cost[1]]
        n = len(cost)
        if n == 2:
            return min(cost)
        for i in range(2, n):
            arr.append(cost[i]+ min(arr[i-1], arr[i-2]))
        return min(arr[n-1],arr[n-2])
