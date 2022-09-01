#
# @lc app=leetcode.cn id=232 lang=python3
#
# [232] 用栈实现队列
#

# @lc code=start
class MyQueue:

    def __init__(self):
        self.a = []
        self.b = []

    def push(self, x: int) -> None:
        self.b.append(x)
        return

    def pop(self) -> int:
        n = len(self.b)
        for _ in range(n - 1):
            self.a.append(self.b.pop())
        res = self.b.pop()
        for _ in range(n - 1):
            self.b.append(self.a.pop())
        return res

    def peek(self) -> int:
        n = len(self.b)
        for _ in range(n - 1):
            self.a.append(self.b.pop())
        res = self.b.pop()
        self.b.append(res)
        for _ in range(n - 1):
            self.b.append(self.a.pop())
        return res

    def empty(self) -> bool:
        return self.b == []


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
# @lc code=end

