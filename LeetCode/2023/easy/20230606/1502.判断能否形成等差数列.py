#
# @lc app=leetcode.cn id=1502 lang=python3
#
# [1502] 判断能否形成等差数列
#

# @lc code=start
class Solution:
    # 思路：先排序
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        arr.sort()
        delta = arr[1] - arr[0]
        n = len(arr)
        for i in range(2, n):
            if arr[i] - arr[i - 1] != delta:
                return False
        return True
# @lc code=end

