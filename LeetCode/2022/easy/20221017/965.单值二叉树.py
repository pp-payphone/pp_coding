#
# @lc app=leetcode.cn id=965 lang=python3
#
# [965] 单值二叉树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        # 递归
        # v = root.val
        # def f(root, val):
        #     if root is None:
        #         return True
        #     elif root.val != val:
        #         return False
        #     else:
        #         return f(root.left, val) and f(root.right, val)
        # return f(root, v)

        # Moriis
        cur = root
        v = root.val
        while cur is not None:
            if cur.val != v:
                return False
            if cur.left is None:
                cur = cur.right
            else:
                max_right = cur.left
                while max_right.right is not None and max_right.right != cur:
                    max_right = max_right.right
                if max_right.right is None:
                    max_right.right = cur
                    cur = cur.left
                else:
                    max_right.right = None
                    cur = cur.right
        return True
# @lc code=end

