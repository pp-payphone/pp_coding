#
# @lc app=leetcode.cn id=859 lang=python3
#
# [859] 亲密字符串
#

# @lc code=start
class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        n1, n2 = len(s), len(goal)
        if n1 != n2:
            return False
        a, b = None, None
        for i in range(n1):
            if s[i] != goal[i]:
                if a is None:
                    a, b = s[i], goal[i]
                elif a == -1:
                    return False
                else:
                    if a != goal[i] or b != s[i]:
                        return False
                    else:
                        a, b = -1, -1
        if a is None:
            return n1 != len(set(s))
        elif a == -1:
            return True
        else:
            return False
# @lc code=end

