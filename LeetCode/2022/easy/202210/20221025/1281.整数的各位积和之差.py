#
# @lc app=leetcode.cn id=1281 lang=python3
#
# [1281] 整数的各位积和之差
#

# @lc code=start
class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        mul = 1
        sum = 0
        while n:
            a = n % 10
            n = n // 10
            mul *= a
            sum += a
        return mul - sum
# @lc code=end

