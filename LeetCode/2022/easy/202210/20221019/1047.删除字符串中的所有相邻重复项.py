#
# @lc app=leetcode.cn id=1047 lang=python3
#
# [1047] 删除字符串中的所有相邻重复项
#

# @lc code=start
class Solution:
    # 72%是认真的？我没有好思路哎！！！！！！！！！！
    ##### 草草草草草 栈啊 我怎么就没想到，这和括号是一样一样的啊！！！
    def removeDuplicates(self, s: str) -> str:
        stack = []
        for each in s:
            if stack == []:
                stack.append(each)
            elif stack[-1] == each:
                stack.pop()
            else:
                stack.append(each)
        return ''.join(stack)

# @lc code=end

