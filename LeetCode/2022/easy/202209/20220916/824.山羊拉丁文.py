#
# @lc app=leetcode.cn id=824 lang=python3
#
# [824] 山羊拉丁文
#

# @lc code=start
class Solution:
    def toGoatLatin(self, sentence: str) -> str:
        res = ''
        first_flag = True
        # word = ''
        word_cnts = 0
        tail = ''
        for s in sentence + ' ':
            if first_flag:
                first_flag = False
                word_cnts += 1
                if s in 'aeiouAEIOU':
                    tail = ''
                    res += s
                else:
                    tail = s
            elif s != ' ':
                res += s
            else:
                first_flag = True
                res += tail
                res += 'ma'
                res += 'a' * word_cnts
                res += ' '
        return res[:-1]

# @lc code=end

