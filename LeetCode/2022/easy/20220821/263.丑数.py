#
# @lc app=leetcode.cn id=263 lang=python3
#
# [263] 丑数
#

# @lc code=start
class Solution:
    # 思路，对这几个因子除啊除
    def isUgly(self, n: int) -> bool:
        # n = -n if n < 0 else n
        if n <= 0:
            return False
        while n % 2 == 0:
            n /= 2
        while n % 3 == 0:
            n /= 3
        while n % 5 == 0:
            n /= 5
        return True if n == 1 else False
# @lc code=end

Solution().isUgly(-2147483648)