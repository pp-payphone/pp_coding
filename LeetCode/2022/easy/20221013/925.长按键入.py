#
# @lc app=leetcode.cn id=925 lang=python3
#
# [925] 长按键入
#

# @lc code=start
class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        m = len(name)
        n = len(typed)
        p, q = 0, 0
        while p < m:
            cnt = 1
            word = name[p]
            p += 1
            while p < m and name[p] == word:
                cnt += 1
                p += 1
            cnt2 = 0
            while q < n and typed[q] == word:
                cnt2 += 1
                q += 1
            if cnt > cnt2:
                return False
        if q != n:
            return False
        else:
            return True
# @lc code=end

