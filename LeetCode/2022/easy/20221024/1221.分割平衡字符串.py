#
# @lc app=leetcode.cn id=1221 lang=python3
#
# [1221] 分割平衡字符串
#

# @lc code=start
class Solution:
    def balancedStringSplit(self, s: str) -> int:
        stack = []
        cnt = 0
        for each in s:
            if stack == [] or stack[-1] == each:
                stack.append(each)
            else:
                stack.pop()
                if stack == []:
                    cnt += 1
        return cnt
# @lc code=end

