#
# @lc app=leetcode.cn id=989 lang=python3
#
# [989] 数组形式的整数加法
#

# @lc code=start
class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        res = []
        A = num
        K = k
        i, carry = len(A) - 1, 0
        while i >= 0 or K != 0:
            x = A[i] if i >= 0 else 0
            y = K % 10 if K != 0 else 0

            sum = x + y + carry
            res.append(sum % 10)
            carry = sum // 10

            i -= 1
            K //= 10
        if carry != 0: res.append(carry)
        return res[::-1]

# @lc code=end

