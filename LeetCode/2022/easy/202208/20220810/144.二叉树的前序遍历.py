#
# @lc app=leetcode.cn id=144 lang=python3
#
# [144] 二叉树的前序遍历
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # # 递归
        # if root is None:
        #     return []
        # return [root.val] + self.preorderTraversal(root.left) + self.preorderTraversal(root.right)
        # 迭代 用到先进后出的栈结构
        if root is None:
            return []
        res = []
        stack = []
        now = root
        while stack != [] or now is not None:
            if now is not None:
                res.append(now.val)
                stack.append(now)
                now = now.left
            else:
                now = stack.pop().right
        return res

# @lc code=end

