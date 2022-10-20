#
# @lc app=leetcode.cn id=653 lang=python3
#
# [653] 两数之和 IV - 输入 BST
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    # 思路：一边从中序遍历正着来，一遍从中序遍历倒着来
    # 一次遍历加上hash的方式可以更快一点点
    def findTarget(self, root, k: int) -> bool:
        # Morris 中序遍历
        cur = root
        l = []
        while cur:
            if cur.left:
                most_right = cur.left
                while most_right.right and most_right.right != cur:
                    most_right = most_right.right
                if most_right.right:
                    most_right.right = None
                    l.append(cur.val)
                    cur = cur.right
                else:
                    most_right.right = cur
                    cur = cur.left
            else:
                l.append(cur.val)
                cur = cur.right
        n = len(l)
        p, q = 0, n-1
        while p != q:
            s = l[p] + l[q]
            if s == k:
                return True
            elif s > k:
                q -= 1
            else:
                p += 1
        return False

# @lc code=end
r1 = TreeNode(2)
r2 = TreeNode(1)
r3 = TreeNode(3)
r1.left = r2
r1.right = r3
Solution().findTarget(r1, 1)