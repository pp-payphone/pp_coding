#
# @lc app=leetcode.cn id=1299 lang=python3
#
# [1299] 将每个元素替换为右侧最大元素
#

# @lc code=start
class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        n = len(arr)
        res = [0 for _ in range(n)]
        max_right = -1
        for i in range(n- 1, -1, -1):
            res[i], max_right = max_right, max(max_right, arr[i])
        return res
# @lc code=end

