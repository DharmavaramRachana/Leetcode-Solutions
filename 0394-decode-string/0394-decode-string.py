class Solution:
    def decodeString(self, s: str) -> str:
        stack = [] #prev , count
        curr = []
        num = 0

        for ch in s:
            if ch.isdigit():
                num = num * 10 + int(ch)

            elif ch == "[":
                stack.append(("".join(curr),num))
                curr = []
                num = 0

            elif ch == "]":
                prev, k = stack.pop()
                curr = [prev + "".join(curr) * k]

            else:
                curr.append(ch)

        return "".join(curr)

        