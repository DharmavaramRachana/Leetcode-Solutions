"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        oldTocopy = {None : None}
        curr = head

        while curr:
            copy = Node(curr.val)
            oldTocopy[curr] = copy
            curr = curr.next

        curr = head
        while curr:
            copy = oldTocopy[curr]
            copy.next = oldTocopy[curr.next]
            copy.random = oldTocopy[curr.random]
            curr = curr.next

        return oldTocopy[head]
        