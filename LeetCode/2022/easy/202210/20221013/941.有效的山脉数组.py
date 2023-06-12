#
# @lc app=leetcode.cn id=941 lang=python3
#
# [941] 有效的山脉数组
#

# @lc code=start
class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        N = len(arr)
        i = 0

        # 递增扫描
        while i + 1 < N and arr[i] < arr[i + 1]:
            i += 1

        # 最高点不能是数组的第一个位置或最后一个位置
        if i == 0 or i == N - 1:
            return False

        # 递减扫描
        while i + 1 < N and arr[i] > arr[i + 1]:
            i += 1

        return i == N - 1


# @lc code=end

