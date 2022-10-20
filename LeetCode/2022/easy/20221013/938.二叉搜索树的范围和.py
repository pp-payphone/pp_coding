#
# @lc app=leetcode.cn id=938 lang=python3
#
# [938] 二叉搜索树的范围和
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rangeSumBST(self, root, low: int, high: int) -> int:
        res = 0
        cur = root
        while cur:
            if cur.val < low:
                cur.left = None
            elif cur.val > high:
                cur.right = None
            if cur.left is None:
                if cur.val >= low and cur.val <= high:
                    res += cur.val
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
                    if cur.val >= low and cur.val <= high:
                        res += cur.val
                    cur = cur.right
        return res
# @lc code=end

r0 = TreeNode(0)
r1 = TreeNode(1)
r2 = TreeNode(2)
r1.left = r0
r1.right = r2
Solution().rangeSumBST(r1, -5, 5)