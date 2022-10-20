#
# @lc app=leetcode.cn id=572 lang=python3
#
# [572] 另一棵树的子树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: TreeNode, subRoot: TreeNode) -> bool:
        if root is None:
            return False
        if self.is_equal(root, subRoot):
            return True
        else:
            return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
        return

    def is_equal(self, r1, r2):
        if r1 is None and r2 is None:
            return True
        elif r1 is None or r2 is None:
            return False
        elif r1.val != r2.val:
            return False
        else:
            return self.is_equal(r1.left, r2.left) and self.is_equal(r1.right, r2.right)

    # 还能更进一步的有更好的算法么？
# @lc code=end

