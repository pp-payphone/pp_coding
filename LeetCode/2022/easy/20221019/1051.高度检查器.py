#
# @lc app=leetcode.cn id=1051 lang=python3
#
# [1051] 高度检查器
#

# @lc code=start
class Solution:
    # 这个场景可以使用计数排序法
    def heightChecker(self, heights: List[int]) -> int:
        n = len(heights)
        cp = [_ for _ in heights]
        cp.sort()
        res = 0
        for i in range(n):
            if cp[i] != heights[i]:
                res += 1
        return res
# @lc code=end

