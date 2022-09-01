#
# @lc app=leetcode.cn id=235 lang=python3
#
# [235] 二叉搜索树的最近公共祖先
#

# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # 思路：先找到p和q的路径，然后同深度下共同的父节点就是最邻近公共祖先
    # 深度优先找路径 debug 了好久 我是个菜鸡
    # 靠！原来二叉搜索树还有这样一个性质，我真是服了我自己个小垃圾
    def lowestCommonAncestor(self, root, p, q):
        path_p = []
        path_q = []
        path = []
        stack = []
        now = root
        while stack != [] or now is not None:
            if path_p != [] and path_q != []:
                break
            if now is not None:
                stack.append(now)
                path.append(now)
                if now == p:
                    path_p = path.copy()
                if now == q:
                    path_q = path.copy()
                now = now.left
            else:
                back = stack.pop()
                now = back.right
                while True:
                    if path.pop() == back:
                        path.append(back)
                        break
                # path.append(now)
        m, n = len(path_p), len(path_q)
        for i in range(min(m, n)):
            if path_p[i] == path_q[i]:
                continue
            else:
                return path_p[i - 1]
        return path_p[min(m, n) - 1]

        
# @lc code=end
r = TreeNode(1)
r.left=TreeNode(2)
r.right=TreeNode(3)
res = Solution().lowestCommonAncestor(r, r.left, r.right)
print(res.val)

