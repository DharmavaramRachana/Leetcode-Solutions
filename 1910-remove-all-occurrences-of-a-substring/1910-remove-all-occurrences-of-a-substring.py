class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        stack = []
        part_length = len(part)

        for char in s:
            stack.append(char)

            if len(stack) >= part_length:
                if "".join(stack[-part_length:]) == part:
                    for _ in range(part_length):
                        stack.pop()

        return "".join(stack)
        