#
# @lc app=leetcode.cn id=605 lang=python3
#
# [605] 种花问题
#

# @lc code=start
class Solution:
    # 边界+连续的0的问题
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        zero_cnts = 1
        res = 0
        for each in flowerbed:
            if each == 0:
                zero_cnts += 1
            else:
                res += (zero_cnts - 1) // 2
                zero_cnts = 0
        res += zero_cnts // 2
        return n <= res
# @lc code=end

