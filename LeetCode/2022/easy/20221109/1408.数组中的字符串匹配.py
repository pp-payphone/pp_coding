#
# @lc app=leetcode.cn id=1408 lang=python3
#
# [1408] 数组中的字符串匹配
#

# @lc code=start
class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        d = {}
        for word in words:
            n = len(word)
            d[n] = d.setdefault(n, []) + [word]
        k = list(d.keys())
        k.sort()
        n = len(k)
        res = []
        for i in range(n - 1):
            for w1 in d[k[i]]:
                f = False
                for j in range(i + 1, n):
                    for w2 in d[k[j]]:
                        if w1 in w2:
                            res.append(w1)
                            f = True
                            break
                    if f:
                        break
        return res
# @lc code=end

