#
# @lc app=leetcode.cn id=205 lang=python3
#
# [205] 同构字符串
#

# @lc code=start
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        map = {}
        target_set = set()
        n = len(s)
        for i in range(n):
            a, b = s[i], t[i]
            m_a = map.get(a)
            if m_a is None and b not in target_set:
                map[a] = b
                target_set.add(b)
            elif m_a is None and b in target_set:
                return False
            elif m_a != b:
                return False
        return True
# @lc code=end

