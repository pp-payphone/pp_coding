#
# @lc app=leetcode.cn id=551 lang=python3
#
# [551] 学生出勤记录 I
#

# @lc code=start
class Solution:
    def checkRecord(self, s: str) -> bool:
        a_cnt = 0
        l_cnt = 0
        for each in s:
            if each == 'P':
                l_cnt = 0
                continue
            elif each == 'L':
                l_cnt += 1
                if l_cnt == 3:
                    return False
            else:
                a_cnt += 1
                l_cnt = 0
                if a_cnt == 2:
                    return False
        return True
# @lc code=end

