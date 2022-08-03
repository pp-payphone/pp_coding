#
# @lc app=leetcode.cn id=105 lang=python3
#
# [105] 从前序与中序遍历序列构造二叉树
#

# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# 前序遍历：DLR
# 中序遍历：LDR
# 后序遍历：LRD
# 层序遍历：

class Solution:
    def buildTree(self, preorder, inorder) -> TreeNode:
        """
        思路：
            1.确定根节点：前序遍历中第一个为根节点
            2.确认左子树和右子树：中序遍历中根节点出现位置以左是左子树，以右是右子树
            3.确认终止条件并递归：
        """
        # return [3,9,20,None,None,15,7]
        n = len(preorder)
        res = TreeNode(preorder[0])
        if n == 1:
            return res
        def find_tree(pre, ino):
            root = pre[0]
            index = ino.index(root)
            left_ino = ino[: index]
            right_ino = ino[index+1 :]
            left_pre, right_pre = [], []
            for each in pre[1:]:
                if each in left_ino:
                    left_pre.append(each)
                else:
                    right_pre.append(each)
            if len(left_pre) > 0:
                left_tree = find_tree(left_pre, left_ino)
            else:
                left_tree = None
            right_tree = find_tree(right_pre, right_ino) if len(right_pre) > 0 else None
            # if left_tree is None and right_tree is None:
            #     return root
            # else:
            return TreeNode(root, left_tree, right_tree)
        res = find_tree(preorder, inorder)
        return res
        
# @lc code=end
s = Solution()
res = s.buildTree([3,9,20,15,7], [9,3,15,20,7])
res
