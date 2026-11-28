# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        num = (n+1)//2
        pick = guess(num)
        l,r = 1, n
        while pick != 0:
            if pick == -1:
                r = num-1
            else:
                l = num+1
            num = (l+r)//2
            pick = guess(num)
        return num
        