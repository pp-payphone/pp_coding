#
# @lc app=leetcode.cn id=1304 lang=python3
#
# [1304] 和为零的 N 个不同整数
#

# @lc code=start
class Solution:
    def sumZero(self, n: int) -> List[int]:
        res = []
        if n % 2 == 0:
            for i in range(1, n // 2 + 1):
                res += [i, -i]
        else:
            res += [0]
            for i in range(1, n // 2 + 1):
                res += [i, -i]
        return res

# @lc code=end

