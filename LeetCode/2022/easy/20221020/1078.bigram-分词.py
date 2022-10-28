#
# @lc app=leetcode.cn id=1078 lang=python3
#
# [1078] Bigram 分词
#

# @lc code=start
class Solution:
    def findOcurrences(self, text: str, first: str, second: str) -> List[str]:
        text_list = text.split(' ')
        n = len(text_list)
        res = []
        if n < 3:
            return res
        for i in range(2, n):
            if text_list[i - 2] == first and text_list[i - 1] == second:
                res.append(text_list[i])
        return res
# @lc code=end

