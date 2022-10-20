#
# @lc app=leetcode.cn id=1022 lang=python3
#
# [1022] 从根到叶的二进制数之和
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        # 迭代+改值
        stack = [root]
        res = 0
        while stack:
            cur = stack[0]
            stack = stack[1:]
            if cur.left is None and cur.right is None:
                res += cur.val
                continue
            if cur.left is not None:
                cur.left.val += cur.val * 2
                stack.append(cur.left)
            if cur.right is not None:
                cur.right.val += cur.val * 2
                stack.append(cur.right)
        return res

# @lc code=end

