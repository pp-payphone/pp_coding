#
# @lc app=leetcode.cn id=1491 lang=python3
#
# [1491] 去掉最低工资和最高工资后的工资平均值
#

# @lc code=start
class Solution:
    def average(self, salary: List[int]) -> float:
        min_s = salary[0]
        max_s = salary[0]
        sum_s = 0
        n = len(salary)
        for s in salary:
            sum_s += s
            if min_s > s:
                min_s = s
            elif max_s < s:
                max_s = s
        return (sum_s - min_s - max_s) / (n - 2)

# @lc code=end

