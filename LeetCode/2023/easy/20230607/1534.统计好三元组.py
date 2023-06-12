#
# @lc app=leetcode.cn id=1534 lang=python3
#
# [1534] 统计好三元组
#

# @lc code=start
class Solution:
    def countGoodTriplets(self, arr, a: int, b: int, c: int) -> int:
        n = len(arr)
        res = 0
        for i in range(n - 2):
            x = arr[i]
            j_left = x - a
            j_right = x + a
            for j in range(i + 1, n - 1):
                y = arr[j]
                if y < j_left or y > j_right:
                    continue
                else:
                    k_left = max(x - c, y - b)
                    k_right = min(x + c, y + b)
                    if k_left > k_right:
                        continue
                for k in range(j + 1, n):
                    z = arr[k]
                    if z >= k_left and z <= k_right:
                        res += 1
                        # print(x, y, z)
        # for i in range(n - 2):
        #     x = arr[i]
        #     for j in range(i + 1, n - 1):
        #         y = arr[j]
        #         for k in range(j + 1, n):
        #             z = arr[k]
        #             if abs(x - y) <= a and abs(y - z) <= b and abs(z - x) <= c:
        #                 res += 1
        #                 print(x, y, z)
        return res
# @lc code=end

res = Solution().countGoodTriplets(arr=[4,4,4,0,0,10,7,8,8], a=8, b=4, c=6)
print(res)