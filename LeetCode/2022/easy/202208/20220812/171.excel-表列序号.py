#
# @lc app=leetcode.cn id=171 lang=python3
#
# [171] Excel 表列序号
#

# @lc code=start
class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        res = 0
        c = 0
        for s in columnTitle[::-1]:
            res += int(ord(s) - ord('A') + 1) * 26 ** c
            c += 1
        return res
# @lc code=end

