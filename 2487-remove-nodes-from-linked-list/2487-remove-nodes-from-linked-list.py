# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def reverse(head):
            prev = None
            curr = head
            while curr:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp

            return prev

        head = reverse(head)

        max_val = head.val
        curr = head

        while curr and curr.next:
            if curr.next.val < max_val:
                # delete node
                curr.next = curr.next.next
            else:
                curr = curr.next
                max_val = curr.val
        
        # Step 3: reverse back
        return reverse(head)
        