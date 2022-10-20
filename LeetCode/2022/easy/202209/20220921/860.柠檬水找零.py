#
# @lc app=leetcode.cn id=860 lang=python3
#
# [860] 柠檬水找零
#

# @lc code=start
class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        d = {5: 0, 10: 0}
        for bill in bills:
            if bill == 5:
                d[5] += 1
            elif bill == 10:
                if d[5] == 0:
                    return False
                else:
                    d[5] -= 1
                    d[10] += 1
            else:
                if d[10] > 0:
                    d[10] -= 1
                    if d[5] > 0:
                        d[5] -= 1
                    else:
                        return False
                else:
                    if d[5] < 3:
                        return False
                    else:
                        d[5] -= 3
        return True
# @lc code=end

