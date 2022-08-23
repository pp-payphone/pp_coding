#
# @lc app=leetcode.cn id=338 lang=python3
#
# [338] 比特位计数
#

# @lc code=start
class Solution:
    # 2,3是在0,1的基础上+1
    # 4 是1
    # 4，5,6,7是在0123的基础上+1

    # 1 -- 0
    # 23 -- 01
    # 4567 -- 0123
    # 1个2个4个8个
    def countBits(self, n: int) -> List[int]:
        res = [0]
        if n == 0:
            return res
        back_cnts = 1
        i = 0
        for _ in range(n):
            if i < back_cnts:
                res.append(res[i] + 1)
                i += 1
            else:
                i = 0
                res.append(res[i] + 1)
                i += 1
                back_cnts *= 2
        return res

# @lc code=end

