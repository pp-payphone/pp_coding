#
# @lc app=leetcode.cn id=434 lang=python3
#
# [434] 字符串中的单词数
#

# @lc code=start
class Solution:
    def countSegments(self, s: str) -> int:
        cnts = 0
        flag = False
        for e in s:
            if e != ' ':
                if flag:
                    continue
                else:
                    flag = True
                    cnts += 1
            else:
                flag = False
        return cnts

# @lc code=end

