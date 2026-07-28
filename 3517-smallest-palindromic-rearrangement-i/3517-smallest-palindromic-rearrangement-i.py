class Solution:
    def smallestPalindrome(self, s: str) -> str:
        count = Counter(s)

        left_half = []
        middle = ""

        for char in sorted(count):
            left_half.append(char * (count[char] // 2))

            if count[char] % 2 == 1:
                middle = char

        left = "".join(left_half)

        return left + middle + left[::-1]