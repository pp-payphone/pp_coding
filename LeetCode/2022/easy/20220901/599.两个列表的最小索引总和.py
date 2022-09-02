#
# @lc app=leetcode.cn id=599 lang=python3
#
# [599] 两个列表的最小索引总和
#

# @lc code=start
class Solution:
    # 方法有很多种，但怎么才能高效
    # 一个hash O(n) O(n)
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        m, n = len(list1), len(list2)
        if m > n:
            list1, list2 = list2, list1
            m, n = n, m
        d = {}
        for idx, each in enumerate(list1):
            d[each] = idx
        res = []
        res_idx = 999999999
        for idx, each in enumerate(list2):
            idx_1 = d.get(each)
            if idx_1 is None:
                continue
            elif idx + idx_1 == res_idx:
                res.append(each)
            elif idx + idx_1 < res_idx:
                res_idx = idx + idx_1
                res = [each]
        return res
# @lc code=end

