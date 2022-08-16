#
# @lc app=leetcode.cn id=225 lang=python3
#
# [225] 用队列实现栈
#

# @lc code=start
class MyStack:
    a = []
    b = []

    def __init__(self):
        self.a = []
        self.b = []

    def push(self, x: int) -> None:
        self.a.append(x)
        for each in self.b:
            self.a.append(each)
        self.b = self.a
        self.a = []
        return

    def pop(self) -> int:
        first = True
        for each in self.b:
            if first:
                res = each
                first = False
            else:
                self.a.append(each)
        self.b = self.a
        self.a = []
        return res

    def top(self) -> int:
        first = True
        for each in self.b:
            if first:
                res = each
                first = False
            self.a.append(each)
        self.b = self.a
        self.a = []
        return res

    def empty(self) -> bool:
        return self.b == []



# Your MyStack object will be instantiated and called as such:
obj = MyStack()
obj.push(1)
obj.push(2)
param_2 = obj.top()
param_3 = obj.pop()
param_4 = obj.empty()
# @lc code=end

