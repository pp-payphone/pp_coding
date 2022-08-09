#
# @lc app=leetcode.cn id=108 lang=python3
#
# [108] 将有序数组转换为二叉搜索树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:

    # 第一想法还是递归思路
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        n = len(nums)
        if n == 1:
            return TreeNode(nums[0])
        elif n == 2:
            return TreeNode(nums[1], left=TreeNode(nums[0]))
        elif n == 3:
            return TreeNode(nums[1], left=TreeNode(nums[0]), right=TreeNode(nums[2]))
        else:
            mid = n // 2
            val = nums[mid]
            left_tree = self.sortedArrayToBST(nums[:mid])
            right_tree = self.sortedArrayToBST(nums[mid + 1:])
            return TreeNode(val, left_tree, right_tree)
# @lc code=end

