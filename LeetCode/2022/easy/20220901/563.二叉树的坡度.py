#
# @lc app=leetcode.cn id=563 lang=python3
#
# [563] 二叉树的坡度
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # 递归
    # 坡度 = 左子树坡度 + 右子树坡度 + 左右子树和的差值的绝对值
    # 递归会造成空间的浪费，最好使用一个方式来保存每个节点的值的和
    # 广度优先逆序赋值
    # 看了标准答案之后恍然大悟，我们只用递归一次就好，累计坡度但是返回树的总值！
    def findTilt(self, root) -> int:
        # def f(root):
        #     if root is None:
        #         return 0
        #     return f(root.left) + f(root.right) + root.val
        # if root is None:
        #     return 0
        # return self.findTilt(root.left) + self.findTilt(root.right) + abs(f(root.left) - f(root.right))

        # from queue import Queue

        # if root is None:
        #     return 0
        # l1 = Queue(-1)
        # l1.put(root)
        # l2 = [root]
        # while not l1.empty():
        #     cur = l1.get()
        #     if cur.left:
        #         l1.put(cur.left)
        #         l2.append(cur.left)
        #     if cur.right:
        #         l1.put(cur.right)
        #         l2.append(cur.right)
        # res = 0
        # while l2 != []:
        #     cur = l2.pop()
        #     v1 = 0 if cur.left is None else cur.left.val
        #     v2 = 0 if cur.right is None else cur.right.val
        #     cur.val += v1 + v2
        #     res += abs(v1 - v2)
        # return res

        if root is None:
            return 0
        self.res = 0

        def f(root):
            if root is None:
                return 0
            vl = f(root.left)
            vr = f(root.right)
            self.res += abs(vl - vr)
            return vl + vr + root.val
        
        f(root)
        return self.res

# @lc code=end

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

r2, r3, r4, r5, r7, r9 = TreeNode(2), TreeNode(3), TreeNode(4), TreeNode(5), TreeNode(7), TreeNode(9)
r2.left = r3
r2.right = r5

r4.left = r2
r4.right = r9

r9.right = r7

root = r4

Solution().findTilt(root)