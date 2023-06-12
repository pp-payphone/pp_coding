#
# @lc app=leetcode.cn id=1021 lang=python3
#
# [1021] 删除最外层的括号
#

# @lc code=start
class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        stack = []
        res = ''
        for each in s:
            if each == '(':
                if stack != []:
                    res += each
                stack.append(each)
            else:
                stack.pop()
                if stack != []:
                    res += each
        return res


# @lc code=end

