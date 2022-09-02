#
# @lc app=leetcode.cn id=637 lang=python3
#
# [637] 二叉树的层平均值
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # 广度优先
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        res = []
        vals = []
        l1, l2 = [root], []
        cur = None
        while l1 != [] or l2 != []:
            if l1 == []:
                res.append(sum(vals) / len(vals))
                vals = []
                while l2:
                    l1.append(l2.pop())
            cur = l1.pop()
            vals.append(cur.val)
            if cur.left:
                l2.append(cur.left)
            if cur.right:
                l2.append(cur.right)
        res.append(sum(vals) / len(vals))
        return res


# @lc code=end

