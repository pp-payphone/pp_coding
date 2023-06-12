#
# @lc app=leetcode.cn id=1175 lang=python3
#
# [1175] 质数排列
#

# @lc code=start
class Solution:
    def numPrimeArrangements(self, n: int) -> int:
        const_list = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97]
        const2 = 10 ** 9 + 7
        c1 = 0
        for each in const_list:
            if each <= n:
                c1 += 1
            else:
                break
        c2 = n - c1
        res = 1
        for i in range(1, c1 + 1):
            res = (res * i) % const2
        for i in range(1, c2 + 1):
            res = (res * i) % const2
        return res
# @lc code=end

