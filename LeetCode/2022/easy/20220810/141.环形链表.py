#
# @lc app=leetcode.cn id=141 lang=python3
#
# [141] 环形链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # 每走一步就给这个节点的值改成一个不会出现的东西，走到尽头就是无环，走到这个值就是有环，但是会破坏链表
    # def hasCycle(self, head: Optional[ListNode]) -> bool:
    #     if head is None:
    #         return False
    #     while head.next:
    #         head.val = -9999999
    #         head = head.next
    #         if head.val == -9999999:
    #             return True
    #     return False

    # 官方答案里给到了一个包括快慢指针的龟兔赛跑算法，很有意思
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head is None:
            return False
        else:
            fast, slow = head, head
            c = 0
            while fast:
                fast = fast.next
                if c % 2 == 1:
                    slow = slow.next
                if fast == slow:
                    return True
                c += 1
            return False

# @lc code=end

