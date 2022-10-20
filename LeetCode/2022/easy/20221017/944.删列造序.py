#
# @lc app=leetcode.cn id=944 lang=python3
#
# [944] 删列造序
#

# @lc code=start
class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        m = len(strs)
        n = len(strs[0])
        res = 0
        for j in range(n):
            for i in range(1, m):
                if strs[i][j] < strs[i - 1][j]:
                    res += 1
                    break
                else:
                    continue
        return res
# @lc code=end

