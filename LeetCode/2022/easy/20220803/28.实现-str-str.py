#
# @lc app=leetcode.cn id=28 lang=python3
#
# [28] 实现 strStr()
#

# @lc code=start
class Solution:
    # 第一想法是直接遍历的思路 O(mn) O(1)
    # 还有一个好神奇的KMP算法，乍一看真的好巧妙，真是完全让人想不到 O(m+n)
    def strStr(self, haystack: str, needle: str) -> int:
        n = len(haystack)
        m = len(needle)
        if m == 0:
            return 0
        elif n < m:
            return -1
        else:
            for p in range(n - m + 1):
                flag = True
                for q in range(m):
                    if haystack[p + q] != needle[q]:
                        flag = False
                        break
                if flag:
                    return p
        return -1
# @lc code=end

