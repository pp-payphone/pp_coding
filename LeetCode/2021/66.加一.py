#
# @lc app=leetcode.cn id=66 lang=python3
#
# [66] 加一
#

# @lc code=start
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        """
        思路：从后往前
        时间复杂度：O(n)
        空间复杂度：O(1)
        """
        n = len(digits)
        for i in range(n-1, -1, -1):
            if digits[i] != 9:
                digits[i] += 1
                return digits
            else:
                digits[i] = 0
        digits[0] = 1
        digits.append(0)
        return digits
# @lc code=end

