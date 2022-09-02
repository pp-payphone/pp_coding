#
# @lc app=leetcode.cn id=661 lang=python3
#
# [661] 图片平滑器
#

# @lc code=start
class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        m = len(img)
        n = len(img[0])
        res = [[0 for _ in range(n)] for _ in range(m)]
        for i in range(m):
            for j in range(n):
                s = 0
                c = 0
                for x in [i-1, i, i+1]:
                    if x >= 0 and x < m:
                        for y in [j-1, j, j+1]:
                            if y >= 0 and y < n:
                                s += img[x][y]
                                c += 1
                res[i][j] = int(s / c)
        return res
# @lc code=end

