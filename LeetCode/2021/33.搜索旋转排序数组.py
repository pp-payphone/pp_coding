#
# @lc app=leetcode.cn id=33 lang=python3
#
# [33] 搜索旋转排序数组
#

# @lc code=start
class Solution:
    def search(self, nums, target: int) -> int:
        """
        思路：
            分情况考虑左右边界和mid的情况（思路是对的，但是不够清晰，二分截断后两侧一定有一侧是有序的）
        时间复杂度：O(logn)
        空间复杂度：O(1)
        """
        n = len(nums)
        left = 0
        right = n-1
        while left < right - 1:
            mid = (left + right)//2
            if nums[mid] == target:
                return mid
            elif target < nums[mid]:
                if nums[left] < nums[right]:
                    right = mid - 1
                elif nums[left] < nums[mid]:
                    if nums[left] <= target:
                        right = mid - 1
                    else:
                        left = mid + 1
                else:
                    right = mid - 1
            elif nums[mid] < target:
                if nums[left] < nums[right]:
                    left = mid + 1
                elif nums[left] < nums[mid]:
                    left = mid + 1
                else:
                    if target <= nums[right]:
                        left = mid + 1
                    else:
                        right = mid -1
        if nums[left] == target:
            return left
        elif nums[right] == target:
            return right
        else:
            return -1
# @lc code=end
s = Solution()
res = s.search([3,5,1], 3)
a = 1
