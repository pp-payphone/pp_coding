#
# @lc app=leetcode.cn id=1346 lang=python3
#
# [1346] 检查整数及其两倍数是否存在
#

# @lc code=start
class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        c = 0
        s = set()
        for each in arr:
            s.add(each)
            if each == 0:
                c += 1
        if c > 1:
            return True
        for each in s:
            if each != 0 and 2 * each in s:
                return True
        return False
# @lc code=end

