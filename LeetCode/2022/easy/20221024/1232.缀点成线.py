#
# @lc app=leetcode.cn id=1232 lang=python3
#
# [1232] 缀点成线
#

# @lc code=start
class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        n = len(coordinates)
        if n <= 2:
            return True
        a, b = coordinates[0], coordinates[1]
        if a[0] == b[0]:
            for each in coordinates[2:]:
                if each[0] != a[0]:
                    return False
            return True
        else:
            k = (b[1] - a[1]) / (b[0] - a[0])
            for each in coordinates[2:]:
                if each[1] != a[1] + k * (each[0] - a[0]):
                    return False
            return True
# @lc code=end

