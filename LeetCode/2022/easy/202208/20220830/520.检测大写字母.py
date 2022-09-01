#
# @lc app=leetcode.cn id=520 lang=python3
#
# [520] 检测大写字母
#

# @lc code=start
class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        low_s = 'qwertyuiopasdfghjklzxcvbnm'
        up_s = low_s.upper()
        if len(word) == 1:
            return True
        if word[0] in low_s:
            for each in word[1:]:
                if each in up_s:
                    return False
            return True
        else:
            if len(word) == 2:
                return True
            if word[1] in low_s:
                for each in word[2:]:
                    if each in up_s:
                        return False
                return True
            else:
                for each in word[2:]:
                    if each in low_s:
                        return False
                return True

# @lc code=end

