# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        arr1 = []
        arr2 = []


        current = list1
        while current:
            arr1.append(current.val)
            current = current.next

        current = list2
        while current:
            arr2.append(current.val)
            current = current.next

        merged = arr1[:a] + arr2 + arr1[b+1:]

        dummy = ListNode()
        current = dummy

        for value in merged:
            current.next = ListNode(value)
            current = current.next

        return dummy.next


