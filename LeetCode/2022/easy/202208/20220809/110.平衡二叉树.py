#
# @lc app=leetcode.cn id=110 lang=python3
#
# [110] 平衡二叉树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # 判断所有叶子结点的深度是否都只差一
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def height(root):
            if root is None:
                return 0
            else:
                l_h = height(root.left)
                r_h = height(root.right)
                if l_h == -1 or r_h == -1 or abs(l_h - r_h) > 1:
                    return -1
                else:
                    return max(l_h, r_h) + 1
        
        return height(root) >= 0





        # def height(root: TreeNode) -> int:
        #     if not root:
        #         return 0
        #     leftHeight = height(root.left)
        #     rightHeight = height(root.right)
        #     if leftHeight == -1 or rightHeight == -1 or abs(leftHeight - rightHeight) > 1:
        #         return -1
        #     else:
        #         return max(leftHeight, rightHeight) + 1

        # return height(root) >= 0

            
# @lc code=end

