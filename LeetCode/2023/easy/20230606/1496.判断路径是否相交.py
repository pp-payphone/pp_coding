#
# @lc app=leetcode.cn id=1496 lang=python3
#
# [1496] 判断路径是否相交
#

# @lc code=start
class Solution:
    # 思路1：走过的路存hash表，但是可能会存很大很大
    # 思路2：任意两点不相同就不相交
    # 呸！结果光官方答案就是用的第一种思路
    def isPathCrossing(self, path: str) -> bool:
        dirs = {
            "N": (-1, 0),
            "S": (1, 0),
            "W": (0, -1),
            "E": (0, 1),
        }
        
        x, y = 0, 0
        vis = set([(x, y)])
        for ch in path:
            dx, dy = dirs[ch]
            x, y = x + dx, y + dy
            if (x, y) in vis:
                return True
            vis.add((x, y))

        return False

# @lc code=end

res = Solution().isPathCrossing('NESWW')
res