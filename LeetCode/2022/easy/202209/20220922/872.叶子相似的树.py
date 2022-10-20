#
# @lc app=leetcode.cn id=872 lang=python3
#
# [872] 叶子相似的树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def get_leaf_list(root):
            if root is None:
                return []
            elif root.left is None and root.right is None:
                return [root.val]
            else:
                return get_leaf_list(root.left) + get_leaf_list(root.right)
        
        l1 = get_leaf_list(root1)
        l2 = get_leaf_list(root2)
        return l1 == l2
# @lc code=end

