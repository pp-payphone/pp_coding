#
# @lc app=leetcode.cn id=219 lang=python3
#
# [219] 存在重复元素 II
#

# @lc code=start
class Solution:
    # 直接思路 hash表加遍历计数 O(n) O(n)
    def containsNearbyDuplicate(self, nums, k: int) -> bool:
        n = len(nums)
        if n == 1 or k == 0:
            return False
        i = 0
        d = {}
        d[nums[0]] = 1
        for j in range(1, n):
            if j - i > k:
                d[nums[i]] -= 1
                i += 1
            count = d.setdefault(nums[j], 0)
            if count != 0:
                return True
            else:
                d[nums[j]] = 1
        return False

# @lc code=end

Solution().containsNearbyDuplicate([1,0,1,1], 1)