class Solution:
    def smallestSubsequence(self, s: str) -> str:
        last_index = {}

       
        for i, char in enumerate(s):
            last_index[char] = i

        stack = []
        in_stack = set()

        for i, char in enumerate(s):

            
            if char in in_stack:
                continue

            
            while (
                stack
                and char < stack[-1]
                and last_index[stack[-1]] > i
            ):
                removed = stack.pop()
                in_stack.remove(removed)

            stack.append(char)
            in_stack.add(char)

        return "".join(stack)