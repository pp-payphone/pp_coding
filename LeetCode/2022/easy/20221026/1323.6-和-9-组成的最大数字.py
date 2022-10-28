#
# @lc app=leetcode.cn id=1323 lang=python3
#
# [1323] 6 和 9 组成的最大数字
#

# @lc code=start
class Solution:
    def maximum69Number (self, num: int) -> int:
        num_s = str(num)
        if '6' in num_s:
            f = True
            res = ''
            for each in num_s:
                if f and each == '6':
                    res += '9'
                    f = False
                else:
                    res += each
        else:
            res = num_s
        return int(res)

# @lc code=end

