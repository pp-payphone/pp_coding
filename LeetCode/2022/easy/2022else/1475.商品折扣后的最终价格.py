#
# @lc app=leetcode.cn id=1475 lang=python3
#
# [1475] 商品折扣后的最终价格
#

# @lc code=start
class Solution:
    def finalPrices(self, prices):
        n = len(prices)
        ans = [0] * n
        st = [0]
        for i in range(n - 1, -1, -1):
            p = prices[i]
            while len(st) > 1 and st[-1] > p:
                st.pop()
            ans[i] = p - st[-1]
            st.append(p)
        return ans

# @lc code=end


Solution().finalPrices([8,4,6,2,3])