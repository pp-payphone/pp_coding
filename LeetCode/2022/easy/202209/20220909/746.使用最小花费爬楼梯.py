#
# @lc app=leetcode.cn id=746 lang=python3
#
# [746] 使用最小花费爬楼梯
#

# @lc code=start
class Solution:
    # 倒序遍历
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        a, b = cost[-2], cost[-1]
        for i in range(n - 3, -1, -1):
            t = cost[i] + min(a, b)
            a, b = t, a
        return min(a, b)
# @lc code=end

