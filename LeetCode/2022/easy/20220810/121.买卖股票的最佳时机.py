#
# @lc app=leetcode.cn id=121 lang=python3
#
# [121] 买卖股票的最佳时机
#

# @lc code=start
class Solution:
    # 最直接的思路是计算每一天购买的最大收益，两层循环 O(n^2)
    # 有没有一次遍历的思路，好好想想
    # 1. 最终结果是两个值，从左向右遍历，保存两个值可行么？
    # 2. 左大右小左小右大两种情况
    # 3. 新来的数字分别三个位置的可能性

    # 我的思路不够只管，虽然对了，其实只用记录每天为止的历史最低价，就可以很快算出当天出售的最高收入，一次遍历完事
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        if n == 1:
            return 0
        else:
            res = 0
            x, y = prices[0], prices[1] # 购买出售价
            for i in range(2, n):
                p = prices[i]
                if x <= y:
                    if p >= y:
                        y = p
                    elif p < y and p >= x:
                        continue
                    else:
                        res = max(res, y - x)
                        x, y = y, p
                else:
                    if p <= y:
                        y = p
                    else:
                        x, y = y, p
            return max(res, y - x)
# @lc code=end

