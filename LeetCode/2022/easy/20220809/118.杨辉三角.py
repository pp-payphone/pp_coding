#
# @lc app=leetcode.cn id=118 lang=python3
#
# [118] 杨辉三角
#

# @lc code=start
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = [[1]]
        for _ in range(numRows-1):
            last_row = res[-1]
            mid = []
            for i in range(len(last_row)-1):
                mid.append(last_row[i] + last_row[i+1])
            res.append([1] + mid + [1])
        return res
# @lc code=end

