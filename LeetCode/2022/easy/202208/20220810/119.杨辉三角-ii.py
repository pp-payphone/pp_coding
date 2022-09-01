#
# @lc app=leetcode.cn id=119 lang=python3
#
# [119] 杨辉三角 II
#

# @lc code=start
class Solution:
    # 使用线性递推公式可以更优，递推公式很有意思啊！牛逼
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [1]
        else:
            pre = [1]
            for _ in range(rowIndex):
                res = []
                for i in range(len(pre)-1):
                    res.append(pre[i] + pre[i + 1])
                res = [1] + res + [1]
                pre = res
        return res
# @lc code=end

