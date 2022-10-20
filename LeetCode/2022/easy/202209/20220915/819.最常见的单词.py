#
# @lc app=leetcode.cn id=819 lang=python3
#
# [819] 最常见的单词
#

# @lc code=start
class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        paragraph = paragraph.lower() + ' '
        # paragraph_list = paragraph.split(' ')
        banned_set = set(banned)
        max_cnts = 0
        res = ''
        paragraph_cnt_dict = {}
        s = ''
        for e in paragraph:
            if e in 'qwertyuiopasdfghjklzxcvbnm':
                s += e
                continue
            else:
                if s in banned_set or s == '':
                    s = ''
                    continue
                else:
                    cnts = paragraph_cnt_dict.setdefault(s, 0) + 1
                    if cnts > max_cnts:
                        max_cnts = cnts
                        res = s
                    paragraph_cnt_dict[s] = cnts
                    s = ''
        return res
                

# @lc code=end

