#
# @lc app=leetcode.cn id=997 lang=python3
#
# [997] 找到小镇的法官
#

# @lc code=start
class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        if n == 1:
            return 1
        trust_cnts = {}
        truted_cnts = {}
        for a, b in trust:
            trust_cnts[a] = trust_cnts.setdefault(a, 0) + 1
            truted_cnts[b] = truted_cnts.setdefault(b, 0) + 1
        for k, v in truted_cnts.items():
            if v == n - 1 and trust_cnts.get(k) is None:
                return k
        return -1

# @lc code=end

