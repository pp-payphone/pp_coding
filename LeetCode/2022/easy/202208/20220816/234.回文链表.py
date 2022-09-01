#
# @lc app=leetcode.cn id=234 lang=python3
#
# [234] 回文链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # 第一个思路是遍历一次，val拿出来，正反对比。 O(n) O(n)
    # 那如何不用额外的空间呢第一想法是计算出长度后各自对比，但是需要O(n^2)时间复杂度
    # 有思路了，在原有基础上对后半段进行翻转，然后对比（我它nnd太牛了啊！居然和官方解答一样！wowow）不过这个方法最好再将最后半部分翻转回原样，同时因为会改变链表结构，不支持多线程并发
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        n = 1
        p = head
        while p.next:
            n += 1
            p = p.next
        if n <= 1:
            return True
        half_n = n // 2
        p = head
        for _ in range((n + 1) // 2):
            p = p.next

        def reverse_list_node(head):
            if head is None:
                return None
            if head.next is None:
                return head
            p, q, w = head, head.next, head.next.next
            p.next = None
            while w is not None:
                q.next = p
                p, q = q, w
                w = q.next
            q.next = p
            return q

        tail = reverse_list_node(p)
        for _ in range(half_n):
            if head.val != tail.val:
                return False
            head = head.next
            tail = tail.next
        return True

# @lc code=end

