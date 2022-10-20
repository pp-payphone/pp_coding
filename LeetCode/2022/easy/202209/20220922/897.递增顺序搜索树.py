#
# @lc app=leetcode.cn id=897 lang=python3
#
# [897] 递增顺序搜索树
#

# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    # 改造moris中序遍历
    def increasingBST(self, root):
        dummy = TreeNode(-1)
        self.prev = dummy
        self.inOrder(root)
        return dummy.right
        
    def inOrder(self, root):
        if not root:
            return None
        self.inOrder(root.left)
        root.left = None
        self.prev.right = root
        self.prev = root
        self.inOrder(root.right)
            
        
# @lc code=end

r0 = TreeNode(0)
r1 = TreeNode(1)
r2 = TreeNode(2)
r3 = TreeNode(3)
r4 = TreeNode(4)
r5 = TreeNode(5)
r6 = TreeNode(6)
r7 = TreeNode(7)
r8 = TreeNode(8)
r9 = TreeNode(9)

r5.left = r3
r5.right = r6
r3.left = r2
r3.right = r4
r6.right = r8
r2.left = r1
r8.left = r7
r8.right = r9

res = Solution().increasingBST(r5)
res