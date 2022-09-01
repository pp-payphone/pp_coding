#
# @lc app=leetcode.cn id=509 lang=python3
#
# [509] 斐波那契数
#

# @lc code=start
class Solution:
    def fib(self, n: int) -> int:
        if n == 0:
            return 0
        a, b = 0, 1
        for _ in range(n - 1):
            a, b = b, a + b
        return b
# @lc code=end

