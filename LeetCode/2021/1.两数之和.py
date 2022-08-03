#
# @lc app=leetcode.cn id=1 lang=python3
#
# [1] 两数之和
#

# @lc code=start
class Solution:
    # def twoSum(self, nums, target):
    #     """
    #     遍历：
    #     时间复杂度：
    #         最坏 = (n-1) + (n-2) + ... + 1 = O(n^2)
    #     空间复杂度：
    #         O(1)
    #     """
    #     l = len(nums)
    #     for i in range(l-1):
    #         for j in range(i+1, l):
    #             if nums[i] + nums[j] == target:
    #                 return [i, j]
    #     return [0]

    def twoSum(self, nums, target):
        """
        哈希表：
        时间复杂度：O(n)
        空间占用量：O(n)
        """
        mid = target / 2
        l = len(nums)
        hash_map = {}
        mid_count = 0
        mid_index = []
        for i in range(l):
            hash_map[nums[i]] = i
            if mid == nums[i]:
                mid_count += 1
                mid_index.append(i)
            if mid_count == 2:
                return mid_index
        for i in range(l):
            x = nums[i]
            y = target - x
            if y == x:
                continue
            if hash_map.setdefault(y):
                return [i, hash_map[y]]
        return [0]

# @lc code=end

