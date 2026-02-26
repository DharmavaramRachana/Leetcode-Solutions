class Solution:
    def numSteps(self, s: str) -> int:
        steps = 0
        carry = 0

        # process from LSB to just before MSB
        for i in range(len(s) - 1, 0, -1):
            bit = (ord(s[i]) - ord('0')) + carry
            if bit % 2 == 0:
                # even -> divide by 2
                steps += 1
            else:
                # odd -> add 1, then divide by 2
                steps += 2
                carry = 1

        # if carry remains, one extra step to reach 1
        return steps + carry