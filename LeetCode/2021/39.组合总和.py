#
# @lc app=leetcode.cn id=39 lang=python3
#
# [39] 组合总和
#

# @lc code=start
from ast import Num


class Solution:
    def combinationSum(self, candidates, target: int):
        """
        思路：
            --拆分+递归+去重可行么？（一共一个....一共n个）（复杂度太高，不可行）
            深度优先的递归回溯，排序后加入早停策略可以加速
        时间复杂度：
        空间复杂度：
        """
        def dfs(t, combine, idx):
            # 终止条件：target<=0或者candidates被全部用完
            if t < 0:
                return 1
            elif idx >= n:
                return
            elif t == 0:
                res.append(combine)
                return
            else:
                for i in range(idx, n):
                    flag = dfs(t-candidates[i], combine + [candidates[i]], i)
                    if flag == 1:
                        break
            return
        candidates.sort()
        res = []
        combine = []
        n = len(candidates)
        dfs(target, combine, 0)
        return res


# @lc code=end

s = Solution()
res = s.combinationSum([2,3,6,7], 7)
res