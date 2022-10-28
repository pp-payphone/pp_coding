#
# @lc app=leetcode.cn id=1200 lang=python3
#
# [1200] 最小绝对差
#

# @lc code=start
class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        res = []
        min_diff = 10 ** 9
        n = len(arr)
        for i in range(n - 1):
            diff = arr[i + 1] - arr[i]
            if diff < min_diff:
                min_diff = diff
                res = [[arr[i], arr[i + 1]]]
            elif diff == min_diff:
                res += [[arr[i], arr[i + 1]]]
        return res
# @lc code=end

