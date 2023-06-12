#
# @lc app=leetcode.cn id=1528 lang=python3
#
# [1528] 重新排列字符串
#

# @lc code=start
class Solution:
    def restoreString(self, s: str, indices) -> str:
        n = len(s)
        res_list = list(s)
        for p in range(n):
            if indices[p] == p:
                continue
            else:
                a = p
                b = indices[p]
                while a != b:
                    res_list[a], res_list[b] = res_list[b], res_list[a]
                    indices[a], indices[b] = indices[b], indices[a]
                    b = indices[a]
        return ''.join(res_list)
# @lc code=end

res = Solution().restoreString("codeleet", [4,5,6,7,0,2,1,3])
res