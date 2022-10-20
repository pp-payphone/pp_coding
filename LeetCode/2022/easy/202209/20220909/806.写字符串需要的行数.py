#
# @lc app=leetcode.cn id=806 lang=python3
#
# [806] 写字符串需要的行数
#

# @lc code=start
class Solution:
    def numberOfLines(self, widths: List[int], s: str) -> List[int]:
        rows = 1
        tail = 0
        for each in s:
            cost = widths[ord(each) - ord('a')]
            if tail + cost > 100:
                rows += 1
                tail = 0
            tail += cost
        return [rows, tail]
# @lc code=end

