#
# @lc app=leetcode.cn id=507 lang=python3
#
# [507] 完美数
#

# @lc code=start
class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        import math
        if num == 1:
            return False
        sum_res = 0
        for i in range(1, int(math.sqrt(num)) + 1):
            if num % i == 0:
                sum_res += i
                if i != 1:
                    sum_res += num // i
        if sum_res == num:
            return True
        else:
            return False
# @lc code=end
res = Solution().checkPerfectNumber(28)
res