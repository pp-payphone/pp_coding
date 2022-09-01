#
# @lc app=leetcode.cn id=125 lang=python3
#
# [125] 验证回文串
#

# @lc code=start
class Solution:
    # 正负同时，遍历一半
    def isPalindrome(self, s: str) -> bool:
        n = len(s)
        if n == 1:
            return True
        else:
            p = 0
            q = n - 1
            while p < q:
                t = True
                if s[p].lower() not in '0123456789qwertyuiopasdfghjklzxcvbnm':
                    p += 1
                    t = False
                if s[q].lower() not in '0123456789qwertyuiopasdfghjklzxcvbnm':
                    q -=1
                    t = False
                if t:
                    if s[p].lower() != s[q].lower():
                        return False
                    p += 1
                    q -= 1
            return True

# @lc code=end

