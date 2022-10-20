#
# @lc app=leetcode.cn id=606 lang=python3
#
# [606] 根据二叉树创建字符串
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # 右边空可以省略，左边空不能省略。叶节点左右都省略
    
    def tree2str(self, root: Optional[TreeNode]) -> str:
        if root is None:
            return ''
        elif root.left is None and root.right is None:
            return '{}'.format(root.val)
        elif root.right is not None:
            return '{}'.format(root.val) + '({})'.format(self.tree2str(root.left)) + '({})'.format(self.tree2str(root.right))
        else:
            return '{}'.format(root.val) + '({})'.format(self.tree2str(root.left))


# @lc code=end

