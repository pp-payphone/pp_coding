#
# @lc app=leetcode.cn id=506 lang=python3
#
# [506] 相对名次
#

# @lc code=start
class Solution:
    # 思路：排序-哈希-替换 O(nlogn) O(n)
    def findRelativeRanks(self, score):
        copy_score = score.copy()
        # copy_score = [1, 2, 3]
        copy_score.sort(reverse=True)
        n = len(copy_score)
        d = {}
        for i, s in enumerate(copy_score):
            d[s] = str(i + 1)
        d[copy_score[0]] = 'Gold Medal'
        if n >= 2:
            d[copy_score[1]] = 'Silver Medal'
        if n >= 3:
            d[copy_score[2]] = 'Bronze Medal'
        for i in range(n):
            score[i] = d[score[i]]
        return score
# @lc code=end

Solution().findRelativeRanks([5,4,3,2,1])