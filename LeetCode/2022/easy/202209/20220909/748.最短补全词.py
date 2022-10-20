#
# @lc app=leetcode.cn id=748 lang=python3
#
# [748] 最短补全词
#

# @lc code=start
class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:
        target_map = {}
        for s in licensePlate:
            if s in 'qwertyuiopasdfghjklzxcvbnm':
                target_map[s] = target_map.setdefault(s, 0) + 1
            elif s in 'QWERTYUIOPASDFGHJKLZXCVBNM':
                s = chr(ord(s) + 32)
                target_map[s] = target_map.setdefault(s, 0) + 1
        res = ''
        res_l = 20
        for word in words:
            word_map = {}
            c = 0
            for s in word:
                c += 1
                word_map[s] = word_map.setdefault(s, 0) + 1
            if c < res_l:
                flag = True
                for k, v in target_map.items():
                    if v <= word_map.setdefault(k, 0):
                        continue
                    else:
                        flag = False
                        break
                if flag:
                    res = word
                    res_l = c
        return res
# @lc code=end

