#
# @lc app=leetcode.cn id=56 lang=python3
#
# [56] 合并区间
#

# @lc code=start
class Solution:
    def merge(self, intervals):
        """
        思路：
            1.先按照左括号从小到大排序
            2.分情况遍历
        时间复杂度：O(nlogn) 排序的时间复杂度
        空间复杂度：O(nlogn) 排序的时间复杂度
        """
        n = len(intervals)
        if n == 1:
            return intervals
        intervals.sort()
        left, right = intervals[0]
        res = []
        for i in range(1, n):
            if right < intervals[i][0]:
                res.append([left, right])
                left, right = intervals[i]
            else:
                right = max(right, intervals[i][1])
        res.append([left, right])
        return res


# @lc code=end

s = Solution()
res = s.merge([[1,3],[2,6],[8,10],[15,18]])
res