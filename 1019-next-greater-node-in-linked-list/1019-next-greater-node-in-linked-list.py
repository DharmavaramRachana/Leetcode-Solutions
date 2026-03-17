# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        values = []

        while head:
            values.append(head.val)
            head = head.next

        n = len(values)
        ans = [0] * n
        stack = []

        for i in range(n):
            while stack and values[i] > values[stack[-1]]:
                idx = stack.pop()
                ans[idx] = values[i]

            stack.append(i)

        return ans