#
# @lc app=leetcode.cn id=242 lang=python3
#
# [242] 有效的字母异位词
#

# @lc code=start
class Solution:
    # 一个hash map储存
    def isAnagram(self, s: str, t: str) -> bool:
        d = {}
        for each in s:
            c = d.setdefault(each, 0)
            d[each] += 1
        for each in t:
            c = d.setdefault(each, 0)
            d[each] -= 1
        for c in d.values():
            if c != 0:
                return False
        return True
# @lc code=end

