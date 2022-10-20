#
# @lc app=leetcode.cn id=884 lang=python3
#
# [884] 两句话中的不常见单词
#

# @lc code=start
class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        d1, d2 = {}, {}
        for word in s1.split(' '):
            d1[word] = d1.setdefault(word, 0) + 1
        for word in s2.split(' '):
            d2[word] = d2.setdefault(word, 0) + 1
        res = []
        for k, v in d1.items():
            if v == 1 and d2.get(k) is None:
                res.append(k)
        for k, v in d2.items():
            if v == 1 and d1.get(k) is None:
                res.append(k)
        return res
# @lc code=end

