#
# @lc app=leetcode.cn id=1507 lang=python3
#
# [1507] 转变日期格式
#

# @lc code=start
class Solution:
    def reformatDate(self, date: str) -> str:
        d, m, y = date.split(' ')
        d = d[:-2]
        if len(d) == 1:
            d = f'0{d}'
        m_dict = dict(zip(["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"], range(1, 13)))
        m = str(m_dict[m])
        if len(m) == 1:
            m = f'0{m}'
        return f'{y}-{m}-{d}'
# @lc code=end

