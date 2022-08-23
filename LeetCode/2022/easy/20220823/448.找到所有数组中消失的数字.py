#
# @lc app=leetcode.cn id=448 lang=python3
#
# [448] 找到所有数组中消失的数字
#

# @lc code=start
class Solution:
    # 遍历+交换？
    # 不用额外空间的思路是相似的，都是李永乐原有数组的空间模拟，我是用了交换顺序的方式，表达用了加上一个数让其真是位置大于n的方法，最终次数会更少一点点
    def findDisappearedNumbers(self, nums):
        # n = len(nums)
        # idx = 0
        # while idx < n:
        #     value = nums[idx]
        #     if value == idx + 1 or value == nums[value - 1]:
        #         idx += 1
        #     else:
        #         nums[idx], nums[value - 1] = nums[value - 1], nums[idx]
        # res = []
        # for i, v in enumerate(nums):
        #     if i + 1 != v:
        #         res.append(i + 1)
        # return res
        n = len(nums)
        for num in nums:
            x = (num - 1) % n
            nums[x] += n
        
        ret = [i + 1 for i, num in enumerate(nums) if num <= n]
        return ret

# @lc code=end

Solution().findDisappearedNumbers([4,3,2,7,8,2,3,1])