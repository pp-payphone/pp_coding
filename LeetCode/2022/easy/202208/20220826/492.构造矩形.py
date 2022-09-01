#
# @lc app=leetcode.cn id=492 lang=python3
#
# [492] 构造矩形
#

# @lc code=start
class Solution:
    def constructRectangle(self, area: int) -> List[int]:
        for w in range(int(area ** 0.5), 0, -1):
            if area % w == 0:
                l = area // w
                return [l, w]
# @lc code=end

