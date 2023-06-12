#
# @lc app=leetcode.cn id=1460 lang=python3
#
# [1460] 通过翻转子数组使两个数组相等
#

# @lc code=start
class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        target.sort()
        arr.sort()
        return target == arr
        # 用hash可以早O(n)时间复杂度下解决，但需要使用额外的空间
# @lc code=end

