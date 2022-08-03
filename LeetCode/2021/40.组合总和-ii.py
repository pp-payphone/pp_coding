#
# @lc app=leetcode.cn id=40 lang=python3
#
# [40] 组合总和 II
#

# @lc code=start
class Solution:
    def combinationSum2(self, candidates, target: int):

        def dfs(target, combine, idx, last_combine_idx):
            if target < 0:
                return -1
            elif target == 0:
                res.append(combine)
                return 
            else:
                for i in range(idx, n):
                    if i+1 != n:
                        ### 这里这会儿不想写了，可以把相同数值的一次性放进来进行递归，idx统一放到除这些外的地方。
                    else:
                    flag = dfs(target-candidates[i], combine + [candidates[i]], i+1)
                    if flag == -1:
                        break
            return
        
        candidates.sort()
        n = len(candidates)
        combine = []
        res = []
        dfs(target, combine, 0)
        return res

# @lc code=end

s = Solution()
res = s.combinationSum2([10,1,2,7,6,1,5], 8)
res