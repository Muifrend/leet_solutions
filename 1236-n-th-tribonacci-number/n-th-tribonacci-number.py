class Solution:
    def tribonacci(self, n: int) -> int:
        tri = [0,1,1]
        if n == 0:
            return 0
        elif n<=2:
            return 1
        for i in range(2,n):
            tri.append(tri[i-2]+tri[i-1]+tri[i])
        return tri[n]

        