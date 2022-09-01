#
# @lc app=leetcode.cn id=504 lang=python3
#
# [504] 七进制数
#

# @lc code=start
class Solution:
    def convertToBase7(self, num: int) -> str:
        if num == 0:
            return '0'
        res = []
        neg = False
        if num < 0:
            neg = True
            num = -num
        while num != 0:
            res.append(str(num % 7))
            num //= 7
        res = ''.join(res[::-1])
        if neg:
            res = '-' + res
        return res
# @lc code=end

