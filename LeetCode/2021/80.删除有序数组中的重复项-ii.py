#
# @lc app=leetcode.cn id=80 lang=python3
#
# [80] 删除有序数组中的重复项 II
#

# @lc code=start
class Solution:
    def removeDuplicates(self, nums) -> int:
        """
        思路：两个指针动起来
        时间复杂度：O(n)
        空间复杂度：O(1)
        """
        n = len(nums)
        if n < 3:
            return n
        p, q = 0, 1
        cnt = 1
        for q in range(1, n):
            if nums[q] == nums[p]:
                if cnt < 2:
                    p += 1
                    nums[p] = nums[q]
                cnt += 1
            else:
                p += 1
                cnt = 1
                nums[p] = nums[q]
        return p+1
# @lc code=end

s = Solution()
res = s.removeDuplicates([1,2,2])
res