#
# @lc app=leetcode.cn id=257 lang=python3
#
# [257] 二叉树的所有路径
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # 深度优先，广度优先两种算法，自己实现的话都是维护一个栈
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        if root.left is None and root.right is None:
            return [str(root.val)]
        res = []
        if root.left:
            for each in self.binaryTreePaths(root.left):
                res.append(str(root.val) + '->' + each)
        if root.right:
            for each in self.binaryTreePaths(root.right):
                res.append(str(root.val) + '->' + each)
        return res
# @lc code=end

