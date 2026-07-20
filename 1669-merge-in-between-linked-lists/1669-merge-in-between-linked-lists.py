# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        dummy = ListNode(0, list1)

        before_a = dummy

        for _ in range(a):
            before_a = before_a.next

        after_b = before_a.next
        for _ in range(b-a+1):
            after_b = after_b.next

        before_a.next = list2
        tail = list2
        while tail.next:
            tail = tail.next

        tail.next = after_b

        return dummy.next