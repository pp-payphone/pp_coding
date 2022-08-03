#
# @lc app=leetcode.cn id=90 lang=python3
#
# [90] 子集 II
#

# @lc code=start
class Solution:
    def subsetsWithDup(self, nums):
        """
        思路：最多n=10，排序很简单，叠加关系加入，一个一个加
        时间复杂度：2^n
        空间复杂度：1
        """
        n = len(nums)
        if n == 1:
            return [[], [nums[0]]]
        nums.sort()
        res = [[], [nums[0]]]
        for i in range(1, n):
            if nums[i] != nums[i-1]:
                for j in range(len(res)):
                    res.append(res[j] + [nums[i]])
            else:
                num = nums[i]
                count = 0
                for j in range(i):
                    if nums[j] == num:
                        count += 1
                for j in range(len(res)):
                    if res[j].count(num) == count:
                        res.append(res[j] + [num])

        return res
# @lc code=end

s = Solution()
res = s.subsetsWithDup([1,2,2])
res