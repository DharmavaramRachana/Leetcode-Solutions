class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split()
        reverse = words[::-1]

        return ' '.join(reverse)
        