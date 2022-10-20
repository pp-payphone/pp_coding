#
# @lc app=leetcode.cn id=762 lang=python3
#
# [762] 二进制表示中质数个计算置位
#

# @lc code=start
class Solution:
    # 思路一，直接遍历，每个数计算有多少个1
    def countPrimeSetBits(self, left: int, right: int) -> int:
        res = 0
        for n in range(left, right + 1):
            c = 0
            while n:
                n = n & (n - 1)
                c += 1
            if c in [2, 3, 5, 7, 11, 13, 17, 19, 23]:
                res += 1
        return res
# @lc code=end

