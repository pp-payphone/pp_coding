#
# @lc app=leetcode.cn id=16 lang=python3
#
# [16] 最接近的三数之和
#

# @lc code=start
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        """
        思路：双指针
        时间复杂度：O(n^2)
        空间复杂度：O(logn)
        """
        n = len(nums)
        nums.sort()
        res = 10e12
        delta = abs(res - target)
        for first in range(n - 2):
            if first > 0 and nums[first] == nums[first - 1]:
                continue
            third = n-1
            second = first + 1
            a = nums[first]
            while second != third:
                b = nums[second]
                c = nums[third]
                three_sum = a + b + c
                if abs(three_sum - target) < delta:
                    res = three_sum
                    delta = abs(three_sum - target)
                if three_sum < target:
                    second += 1
                elif three_sum > target:
                    third -= 1
                else:
                    return target
        return res








# @lc code=end

