#
# @lc app=leetcode.cn id=1128 lang=python3
#
# [1128] 等价多米诺骨牌对的数量
#

# @lc code=start
class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        # n = len(dominoes)
        # for i, each in enumerate(dominoes):
        #     x, y = each
        #     if x > y:
        #         dominoes[i] = [y, x]
        # dominoes.sort()
        # res = 0
        # p = 0
        # c = 1
        # while p < n - 1:
        #     if dominoes[p] == dominoes[p + 1]:
        #         c += 1
        #     else:
        #         res += c * (c - 1) // 2
        #         c = 1
        #     p += 1
        # return res + c * (c - 1) // 2

        num = [0] * 100
        ret = 0
        for x, y in dominoes:
            val = (x * 10 + y if x <= y else y * 10 + x)
            ret += num[val]
            num[val] += 1
        return ret

# @lc code=end

