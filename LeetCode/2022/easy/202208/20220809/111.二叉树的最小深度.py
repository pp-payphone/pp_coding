#
# @lc app=leetcode.cn id=111 lang=python3
#
# [111] 二叉树的最小深度
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        elif root.left is not None and root.right is not None:
            return min(self.minDepth(root.left), self.minDepth(root.right)) + 1
        elif root.left is not None:
            return self.minDepth(root.left) + 1
        else:
            return self.minDepth(root.right) + 1
# @lc code=end

