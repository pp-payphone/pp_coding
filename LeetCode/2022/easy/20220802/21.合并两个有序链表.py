#
# @lc app=leetcode.cn id=21 lang=python3
#
# [21] 合并两个有序链表
#

# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    # 我这里其实用到了迭代的思想，但写的不够简洁 O(m+n) O(1)
    # 还有用递归的思维也可以求解， O(m+n) O(m+n)
    def mergeTwoLists(self, list1, list2):
        if list1 is None:
            return list2
        elif list2 is None:
            return list1
        if list1.val <= list2.val:
            head = list1
            now = head
            list1 = list1.next
        else:
            head = list2
            now = head
            list2 = list2.next
        while (list1 is not None) and (list2 is not None):
            if list1.val <= list2.val:
                now.next = list1
                now = list1
                list1 = list1.next
            else:
                now.next = list2
                now = list2
                list2 = list2.next
        if list1 is not None:
            now.next = list1
        elif list2 is not None:
            now.next = list2

        return head
# @lc code=end
a = ListNode(1, ListNode(2, ListNode(4)))
b = ListNode(1, ListNode(2, ListNode(4)))
Solution().mergeTwoLists(a, b)