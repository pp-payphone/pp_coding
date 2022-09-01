#
# @lc app=leetcode.cn id=290 lang=python3
#
# [290] 单词规律
#

# @lc code=start
class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        word_list = s.split(' ')
        if len(pattern) != len(word_list):
            return False
        m = {}
        used_words = set()
        for i, p in enumerate(pattern):
            word = word_list[i]
            if m.get(p) is None:
                if word not in used_words:
                    used_words.add(word)
                    m[p] = word
                else:
                    return False
            elif m.get(p) != word:
                return False
        return True
# @lc code=end

Solution().wordPattern('abba', "dog cat cat dog")