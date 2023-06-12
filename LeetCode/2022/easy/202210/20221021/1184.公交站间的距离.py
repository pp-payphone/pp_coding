#
# @lc app=leetcode.cn id=1184 lang=python3
#
# [1184] 公交站间的距离
#

# @lc code=start
class Solution:
    def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:
        d1 = 0
        d2 = 0
        s = min(start, destination)
        des = max(start, destination)
        for i, d in enumerate(distance):
            if i >= s and i < des:
                d1 += d
            else:
                d2 += d
        return min(d1, d2)
# @lc code=end

