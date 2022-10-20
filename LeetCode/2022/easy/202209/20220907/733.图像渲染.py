#
# @lc app=leetcode.cn id=733 lang=python3
#
# [733] 图像渲染
#

# @lc code=start
class Solution:
    def floodFill(self, image, sr, sc, color):
        m = len(image)
        n = len(image[0])
        orig_color = image[sr][sc]
        if orig_color == color:
            return image

        def f(image, r, c, color):
            image[r][c] = color
            if r > 0 and image[r - 1][c] == orig_color:
                f(image, r - 1, c, color)
            if r < m - 1 and image[r + 1][c] == orig_color:
                f(image, r + 1, c, color)
            if c > 0 and image[r][c - 1] == orig_color:
                f(image, r, c - 1, color)
            if c < n - 1 and image[r][c + 1] == orig_color:
                f(image, r, c + 1, color)
        f(image, sr, sc, color)
        return image
        
# @lc code=end
