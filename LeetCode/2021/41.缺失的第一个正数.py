#
# @lc app=leetcode.cn id=41 lang=python3
#
# [41] 缺失的第一个正数
#

# @lc code=start
class Solution:
    def firstMissingPositive(self, nums) -> int:
        """
        思路：
            由于要求我们只能使用O(1)的空间，所以我们可以考虑使用列表原本的空间。（否则不使用额外空间的情况下的算法是不存在的）
            1.通过对index=i的位置的数标负号来标识该数字是否存在于数组中
            2.通过递归交换每个数到其对应的位子为止来进行标识。
        时间复杂度：
        空间复杂度：
        """
        n = len(nums)
        for i in range(n): # 所有负数和0统一变为数值n+1
            if nums[i] < 1:
                nums[i] = n+1
        for i in range(n):
            if 0 < abs(nums[i]) <= n:
                if nums[abs(nums[i])-1] > 0:
                    nums[abs(nums[i])-1] *= -1
        flag = False
        for i in range(n):
            if nums[i] >= 0:
                flag = True
                break
        if flag:
            return i + 1
        else:
            return n+1
        

# @lc code=end

s = Solution()
res = s.firstMissingPositive([1])
res