#
# @lc app=leetcode.cn id=482 lang=python3
#
# [482] 密钥格式化
#

# @lc code=start
class Solution:
    # 倒着来可以一次遍历
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        c = 0
        res = ''
        for each in s[::-1]:
            if each != '-':
                if c == k:
                    res = '-' + res
                    c = 0
                res = each + res
                c += 1
        return res.upper()

# @lc code=end

