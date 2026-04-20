class Node:
    def __init__(self,start,end):
        self.start = start
        self.end = end
        self.left = None
        self.right = None
        
class MyCalendar:

    def __init__(self):
        self.root = None
        

    def book(self, start: int, end: int) -> bool:
        if not self.root:
            self.root = Node(start, end)
            return True

        curr = self.root

        while True:

            if end <= curr.start:
                if curr.left is None:
                    curr.left = Node(start, end)
                    return True

                curr = curr.left 

            elif start >= curr.end:
                if curr.right is None:
                    curr.right = Node(start, end)
                    return True

                curr = curr.right

            else:
                return False


        


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(startTime,endTime)