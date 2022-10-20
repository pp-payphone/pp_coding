#
# @lc app=leetcode.cn id=933 lang=python3
#
# [933] 最近的请求次数
#

# @lc code=start
class RecentCounter:

    def __init__(self):
        self.pings = []
        return

    def ping(self, t: int) -> int:
        self.pings.append(t)
        for i in range(len(self.pings)):
            if self.pings[i] >= t-3000:
                break
        self.pings = self.pings[i:]
        return len(self.pings)



# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)
# @lc code=end

