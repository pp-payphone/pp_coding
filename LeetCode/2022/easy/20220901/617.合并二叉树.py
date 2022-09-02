#
# @lc app=leetcode.cn id=617 lang=python3
#
# [617] 合并二叉树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
    # def __init__(self, val=0, left=None, right=None):
    #     self.val = val
    #     self.left = left
    #     self.right = right
class Solution:
    # 好像不适合递归
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        if root1 is None:
            return root2
        elif root2 is None:
            return root1
        l = []
        cur1, cur2 = root1, root2
        while cur1 is not None or cur2 is not None or l != []:
            if cur1 is None and cur2 is None:
                cur1, cur2 = l.pop()
                if cur2.right is not None and cur1.right is None:
                    cur1.right = TreeNode()
                cur1 = cur1.right
                cur2 = cur2.right
            elif cur1 is None:
                cur1 = TreeNode(cur2.val)
                l.append([cur1, cur2])
                if cur2.left is not None and cur1.left is None:
                    cur1.left = TreeNode()
                cur1 = cur1.left
                cur2 = cur2.left
            elif cur2 is None:
                cur2 = TreeNode(0)
                l.append([cur1, cur2])
                if cur2.left is not None and cur1.left is None:
                    cur1.left = TreeNode()
                cur1 = cur1.left
                cur2 = cur2.left
            else:
                cur1.val += cur2.val
                l.append([cur1, cur2])
                if cur2.left is not None and cur1.left is None:
                    cur1.left = TreeNode()
                cur1 = cur1.left
                cur2 = cur2.left
        return root1

# @lc code=end

