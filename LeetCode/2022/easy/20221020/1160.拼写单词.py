#
# @lc app=leetcode.cn id=1160 lang=python3
#
# [1160] 拼写单词
#

# @lc code=start
class Solution:
    def countCharacters(self, words, chars: str) -> int:
        char_dict = {}
        for each in chars:
            char_dict[each] = char_dict.setdefault(each, 0) + 1
        res = 0
        for word in words:
            f = True
            word_dict = {}
            for each in word:
                cnt = word_dict.setdefault(each, 0) + 1
                if char_dict.setdefault(each, 0) < cnt:
                    f = False
                    break
                else:
                    word_dict[each] = cnt
            if f:
                res += len(word)
        return res
# @lc code=end

Solution().countCharacters(["cat","bt","hat","tree"], "atach")