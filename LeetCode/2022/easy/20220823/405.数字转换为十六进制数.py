#
# @lc app=leetcode.cn id=405 lang=python3
#
# [405] 数字转换为十六进制数
#

# @lc code=start
class Solution:
    def toHex(self, num: int) -> str:
        CONV = "0123456789abcdef"
        ans = []
        for _ in range(8):
            ans.append(num%16)
            num //= 16
            if not num:
                break
        return "".join(CONV[n] for n in ans[::-1])
# @lc code=end

