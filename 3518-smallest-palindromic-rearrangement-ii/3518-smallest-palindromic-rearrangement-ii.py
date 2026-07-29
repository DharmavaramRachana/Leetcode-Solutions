from collections import Counter
from math import comb


class Solution:
    def smallestPalindrome(self, s: str, k: int) -> str:
        if k <= 0:
            return ""

        frequency = Counter(s)

        middle = ""
        half_count = {}

        for char, count in frequency.items():
            half_count[char] = count // 2

            if count % 2 == 1:
                if middle:
                    return ""  # Safety check
                middle = char

        chars = sorted(half_count)
        remaining = sum(half_count.values())

        # Number of distinct permutations of the first half.
        ways = 1
        used = 0

        for char in chars:
            count = half_count[char]
            ways *= comb(used + count, count)
            used += count

        # Not enough distinct palindromic permutations.
        if k > ways:
            return ""

        first_half = []

        while remaining > 0:
            for char in chars:
                count = half_count[char]

                if count == 0:
                    continue

                # Number of permutations beginning with this character.
                block_size = ways * count // remaining

                if k > block_size:
                    # Skip every palindrome beginning with this character.
                    k -= block_size
                else:
                    first_half.append(char)
                    half_count[char] -= 1

                    ways = block_size
                    remaining -= 1
                    break

        first_half = "".join(first_half)

        return first_half + middle + first_half[::-1]