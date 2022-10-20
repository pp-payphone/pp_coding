#
# @lc app=leetcode.cn id=594 lang=python3
#
# [594] 最长和谐子序列
#

# @lc code=start
class Solution:
    # 排序的时间复杂度为nlogn；也可以用hash的方法空间换时间，压缩时间到O(n)
    def findLHS(self, nums) -> int:
        res = 0
        n = len(nums)
        nums.sort()
        x, y = -10**10, -10**10
        x_cnt, y_cnt = 0, 0
        for each in nums:
            if each == y:
                y_cnt += 1
            elif each == y + 1:
                res = max(res, 0 if x_cnt == 0 else x_cnt + y_cnt)
                x, y = y, each
                x_cnt = y_cnt
                y_cnt = 1
            else:
                res = max(res, 0 if x_cnt == 0 else x_cnt + y_cnt)
                x, y = y, each
                x_cnt = 0
                y_cnt = 1
        return max(res, 0 if x_cnt == 0 else x_cnt + y_cnt)

# @lc code=end

Solution().findLHS([1,3,2,2,5,2,3,7])