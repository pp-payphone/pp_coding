#
# @lc app=leetcode.cn id=589 lang=python3
#
# [589] N 叉树的前序遍历
#

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    # 递归完事了
    def preorder(self, root: 'Node') -> List[int]:
        if root is None:
            return []
        res = [root.val]
        for child in root.children:
            res += self.preorder(child)
        return res
# @lc code=end

