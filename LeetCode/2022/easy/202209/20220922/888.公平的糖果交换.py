#
# @lc app=leetcode.cn id=888 lang=python3
#
# [888] 公平的糖果交换
#

# @lc code=start
class Solution:
    def fairCandySwap(self, aliceSizes: List[int], bobSizes: List[int]) -> List[int]:
        s1 = sum(aliceSizes)
        s2 = sum(bobSizes)
        diff = (s2 - s1) // 2
        s = set(bobSizes)
        for each in aliceSizes:
            if (each + diff) in s:
                return [each, each + diff]

# @lc code=end

