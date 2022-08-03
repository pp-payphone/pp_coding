#
# @lc app=leetcode.cn id=57 lang=python3
#
# [57] 插入区间
#

# @lc code=start
class Solution:
    def insert(self, intervals, newInterval):
        """
        思路：
            所有和新区间重合的区间合并成一个大区间即可
        时间复杂度：O(n)
        空间复杂度：O(1)
        """
        left, right = newInterval
        placed = False
        ans = list()
        for li, ri in intervals:
            if li > right:
                # 在插入区间的右侧且无交集
                if not placed:
                    ans.append([left, right])
                    placed = True
                ans.append([li, ri])
            elif ri < left:
                # 在插入区间的左侧且无交集
                ans.append([li, ri])
            else:
                # 与插入区间有交集，计算它们的并集
                left = min(left, li)
                right = max(right, ri)
        
        if not placed:
            ans.append([left, right])
        return ans


# @lc code=end

s = Solution()
res = s.insert([[1,2],[3,5],[6,7],[8,10],[12,16]], [4,8])
res