#
# @lc app=leetcode.cn id=190 lang=python3
#
# [190] 颠倒二进制位
#

# @lc code=start
class Solution:
    def reverseBits(self, n: int) -> int:
        s = bin(n)[2:]
        s = (32 - len(s)) * '0' + s
        return int(s[::-1], 2)
# @lc code=end

