#
# @lc app=leetcode.cn id=31 lang=python3
#
# [31] 下一个排列
#

# @lc code=start
class Solution:
    def nextPermutation(self, nums) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        """
        思路:
            左边的较小数和右边的较大数交换
            左边的较小数需要尽量靠右（从右往左的第一个逆序对）
            右边的较大数要尽可能小
            交换后较大数后面的数重排
        时间复杂度:O(n)
        空间复杂度:O(1)
        """
        n = len(nums)
        if n == 1:
            return
        left = None
        for i in range(n-1, 0, -1):
            if nums[i-1] < nums[i]:
                left = i-1
                break
        if left is None:
            # 没有逆序，交换
            for i in range(n//2):
                t = nums[i]
                nums[i] = nums[n-1-i]
                nums[n-1-i] = t
            return
        else:
            for j in range(n-1, left, -1):
                if nums[left] < nums[j]:
                    right = j
                    break
            t = nums[left]
            nums[left] = nums[right]
            nums[right] = t
            # 后半段已经降序，直接倒序就行
            for i in range((n-left-1)//2):
                t = nums[left+1+i]
                nums[left+1+i] = nums[n-1-i]
                nums[n-1-i] = t
            return
# @lc code=end

s = Solution()
s.nextPermutation([2,3,1])