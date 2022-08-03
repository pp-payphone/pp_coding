#
# @lc app=leetcode.cn id=66 lang=python3
#
# [66] 加一
#

# @lc code=start
class Solution:
    # 第一想法是倒序遍历，然后处理进位的情况 O(n) O(1)
    def plusOne(self, digits: List[int]) -> List[int]:
        n = len(digits)
        for i in range(n-1, -1, -1):
            if digits[i] == 9:
                digits[i] = 0
                continue
            else:
                digits[i] += 1
                return digits
        return [1] + digits
        
# @lc code=end

