class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        s = set(word)

        count = 0

        for ch in range(26):
            lower = chr(ord('a') + ch)
            upper = chr(ord('A') + ch)

            if lower in s and upper in s:
                count += 1

        return count