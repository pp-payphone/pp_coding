#
# @lc app=leetcode.cn id=783 lang=python3
#
# [783] 二叉搜索树节点最小距离
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # 思路：中序遍历保存前后差值
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        a, b = None, None
        cur = root
        res = 10 ** 7
        while cur:
            if cur.left:
                max_right = cur.left
                while max_right.right and max_right.right != cur:
                    max_right = max_right.right
                if max_right.right is None:
                    max_right.right = cur
                    cur = cur.left
                    continue
                else:
                    max_right.right = None
                    c = cur.val
                    cur = cur.right
            else:
                c = cur.val
                cur = cur.right
            if a is not None:
                res = min(b - a, res)
                a, b = b, c
            else:
                a, b = b, c
        return min(b - a, res)
            

# @lc code=end

