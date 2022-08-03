#
# @lc app=leetcode.cn id=18 lang=python3
#
# [18] 四数之和
#

# @lc code=start
class Solution:
    def fourSum(self, nums, target):
        """
        思路:三指针遍历，思路同三数相加
        时间复杂度:O(n^3)
        空间复杂度:O(logn)
        """
        n = len(nums)
        if n < 4:
            return []
        nums.sort()
        res = []
        for first in range(n-3):
            a = nums[first]
            if first > 0 and nums[first] == nums[first-1]:
                continue
            for second in range(first+1, n-2):
                b = nums[second]
                if second > first+1 and nums[second] == nums[second-1]:
                    continue
                third = second + 1
                fourth = n - 1
                while third != fourth:
                    if third > second + 1 and nums[third] == nums[third -1]:
                        third += 1
                        continue
                    elif fourth < n-1 and nums[fourth] == nums[fourth+1]:
                        fourth -= 1
                        continue
                    elif a + b + nums[third] + nums[fourth] == target:
                        res.append([a, b, nums[third], nums[fourth]])
                        third += 1
                    elif a + b + nums[third] + nums[fourth] < target:
                        third += 1
                    elif a + b + nums[third] + nums[fourth] > target:
                        fourth -= 1
        return res
                        

# @lc code=end

s = Solution()
res = s.fourSum([1,0,-1,0,-2,2], 0)
print(res)