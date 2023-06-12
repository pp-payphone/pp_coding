#
# @lc app=leetcode.cn id=1379 lang=python3
#
# [1379] 找出克隆二叉树中的相同节点
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        cur1 = original
        cur2 = cloned
        while cur1 is not None:
            if cur1 == target:
                res = cur2
            if cur1.left is not None:
                max_right1 = cur1.left
                max_right2 = cur2.left
                while max_right1.right is not None and max_right1.right != cur1:
                    max_right1 = max_right1.right
                    max_right2 = max_right2.right
                if max_right1.right is None:
                    max_right1.right = cur1
                    max_right2.right = cur2
                    cur1 = cur1.left
                    cur2 = cur2.left
                else:
                    max_right1.right = None
                    max_right2.right = None
                    cur1 = cur1.right
                    cur2 = cur2.right
            else:
                cur1 = cur1.right
                cur2 = cur2.right

        return res
        
# @lc code=end

