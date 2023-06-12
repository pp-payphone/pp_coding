#
# @lc app=leetcode.cn id=1207 lang=python3
#
# [1207] 独一无二的出现次数
#

# @lc code=start
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        d = {}
        for each in arr:
            d[each] = d.setdefault(each, 0) + 1
        l = list(d.values())
        return len(l) == len(set(l))
# @lc code=end

