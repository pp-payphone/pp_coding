#
# @lc app=leetcode.cn id=914 lang=python3
#
# [914] 卡牌分组
#

# @lc code=start
class Solution:
    def hasGroupsSizeX(self, deck) -> bool:
        d = {}
        for each in deck:
            d[each] = d.setdefault(each, 0) + 1
        s = set(d.values())
        m = min(s)
        if m == 1:
            return False
        else:
            for i in range(2, m + 1):
                f = True
                if m % i == 0:
                    for each in s:
                        if each % i != 0:
                            f = False
                            break
                else:
                    continue
                if f:
                    return True
            return False
# @lc code=end

Solution().hasGroupsSizeX([1,1,1,1,1,0,0,0])