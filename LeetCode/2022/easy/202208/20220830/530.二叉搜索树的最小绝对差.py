#
# @lc app=leetcode.cn id=530 lang=python3
#
# [530] 二叉搜索树的最小绝对差
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # 递归（我的思路有个问题是右子树汇总最小的和根节点的差才是最小绝对差，而不是右子树的根节点和根节点的差）
    # 思路二：中序遍历后依次最小差值，那是不是可以用那个神奇的算法
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        # if root is None:
        #     return 100000
        # left_gap = 100000 if root.left is None else root.val - root.left.val
        # right_gap = 100000 if root.right is None else root.right.val - root.val
        # return min(self.getMinimumDifference(root.left), self.getMinimumDifference(root.right), left_gap, right_gap)

        # # 递归中序遍历的方法
        # def f(root):
        #     if root is None:
        #         return []
        #     return f(root.left) + [root.val] + f(root.right)

        # mid = f(root)
        # res = 100000
        # for i in range(len(mid) - 1):
        #     res = min(res, mid[i + 1] - mid[i])
        # return res

        # morris 中序遍历大法！冲！
        a, b = -1000000, -1000000
        res = 1000000
        cur = root
        while cur:
            if cur.left is not None:
                left_max_right = cur.left
                while left_max_right.right is not None and left_max_right.right != cur:
                    left_max_right = left_max_right.right
                if left_max_right.right is None:
                    left_max_right.right = cur
                    cur = cur.left
                else:
                    left_max_right.right = None
                    a, b = b, cur.val
                    res = min(res, b - a)
                    cur = cur.right
                # while True:
                #     if left_max_right.right is None:
                #         left_max_right.right = cur
                #         cur = cur.left
                #         break
                #     elif left_max_right.right == cur:
                #         left_max_right.right = None
                #         a, b = b, cur.val
                #         res = min(res, b - a)
                #         cur = cur.right
                #         break
                #     else:
                #         left_max_right = left_max_right.right
            else:
                a, b = b, cur.val
                res = min(res, b - a)
                cur = cur.right
        return res

        
# @lc code=end

