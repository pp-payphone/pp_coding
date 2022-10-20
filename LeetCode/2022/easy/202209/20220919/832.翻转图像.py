#
# @lc app=leetcode.cn id=832 lang=python3
#
# [832] 翻转图像
#

# @lc code=start
class Solution:
    def flipAndInvertImage(self, image):
        m = len(image)
        n = len(image[0])
        for row in image:
            p, q = 0, n - 1
            while p < q:
                row[p], row[q] = 1 - row[q], 1 - row[p]
                p += 1
                q -= 1
            if p == q:
                row[p] = 1 - row[p]
        return image

# @lc code=end

Solution().flipAndInvertImage([[1,1,0],[1,0,1],[0,0,0]])