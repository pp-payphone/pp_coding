#
# @lc app=leetcode.cn id=217 lang=python3
#
# [217] 存在重复元素
#

# @lc code=start
class Solution:
    # 最直接的思路，遍历加哈希表 O(n) O(n)
    def containsDuplicate(self, nums: List[int]) -> bool:
        d = {}
        for num in nums:
            n = d.get(num)
            if n is not None:
                return True
            else:
                d[num] = 1
        return False
# @lc code=end

