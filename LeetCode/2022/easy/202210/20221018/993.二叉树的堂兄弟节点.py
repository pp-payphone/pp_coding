#
# @lc app=leetcode.cn id=993 lang=python3
#
# [993] 二叉树的堂兄弟节点
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        # 广度优先
        a = [root]
        b = []
        find_x, find_y = False, False
        if root.val == x or root.val == y:
            return False
        while a:
            for each in a:
                l = each.left
                r = each.right
                if l is not None:
                    b.append(l)
                    v1 = l.val
                else:
                    v1 = 0
                if r is not None:
                    b.append(r)
                    v2 = r.val
                else:
                    v2 = 0
                if (v1 == x and v2 == y) or (v1 == y and v2 == x):
                    return False
                elif find_x and (v1 == y or v2 == y):
                    return True
                elif find_y and (v1 == x or v2 == x):
                    return True
                elif v1 == x or v2 == x:
                    find_x = True
                elif v1 == y or v2 == y:
                    find_y = True
            if find_x or find_y:
                return False
            a, b = b, []
        return False

# @lc code=end

