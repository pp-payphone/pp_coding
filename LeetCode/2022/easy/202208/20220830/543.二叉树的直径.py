#
# @lc app=leetcode.cn id=543 lang=python3
#
# [543] 二叉树的直径
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # 思路：递归？
    # 左子树直径，右子树直径，通过根节点的直径，三个取max
    # 其中通过根节点的直径有需要左右各自的最长深度,然后计算获得
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def f(root):  # 树直径，当前最大深度
            if root is None:
                return 0, 0
            d_left, deep_left = f(root.left)
            d_right, deep_right = f(root.right)
            return max(d_left, d_right, deep_left + deep_right + 1), max(deep_left, deep_right) + 1
        return f(root)[0] - 1
# @lc code=end

