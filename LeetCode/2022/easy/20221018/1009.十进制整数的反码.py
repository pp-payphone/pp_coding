#
# @lc app=leetcode.cn id=1009 lang=python3
#
# [1009] 十进制整数的反码
#

# @lc code=start
class Solution:
    def bitwiseComplement(self, n: int) -> int:
        a = bin(n)
        b = ''
        for s in a[2:]:
            b += '0' if s == '1' else '1'
        return int(b, 2)
# @lc code=end

