#
# @lc app=leetcode.cn id=374 lang=python3
#
# [374] 猜数字大小
#

# @lc code=start
# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num: int) -> int:

class Solution:
    # 二分法
    def guessNumber(self, n: int) -> int:
        if guess(1) == 0:
            return 1
        if guess(n) == 0:
            return n
        x, y = 1, n
        while True:
            mid_l = (x + y) // 2
            ans = guess(mid_l)
            if ans == -1:
                y = mid_l
            elif ans == 1:
                x = mid_l
            else:
                return mid_l
        
# @lc code=end

