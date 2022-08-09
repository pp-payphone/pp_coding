#
# @lc app=leetcode.cn id=101 lang=python3
#
# [101] 对称二叉树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # 其实就是再上一题的基础上判断左右两个子树是否相同
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        else:
            return self.isSymmetricTree(root.left, root.right)

    def isSymmetricTree(self, p, q):
        if p is None and q is None:
            return True
        elif p is not None and q is not None and p.val == q.val:
            return self.isSymmetricTree(p.left, q.right) and self.isSymmetricTree(p.right, q.left)
        else:
            return False
# @lc code=end

