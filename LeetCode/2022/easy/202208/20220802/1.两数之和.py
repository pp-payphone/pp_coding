#
# @lc app=leetcode.cn id=1 lang=python3
#
# [1] 两数之和
#

# @lc code=start
class Solution:
    # 直接思路，两层遍历 O(n^2) O(n^2)
    # 空间换时间 O(n) O(n)
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        bak_res_dict = {}
        res = []
        for i in range(len(nums)):
            a = nums[i]
            b = target - a
            if bak_res_dict.get(b) is None:
                bak_res_dict[a] = i
            else:
                res = [i, bak_res_dict.get(b)]
                break
        return res
# @lc code=end

