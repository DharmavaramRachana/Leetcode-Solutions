class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = "aeiou"
        i = 0
        count = 0

        while i < k:
            if s[i] in vowels:
                count += 1

            i += 1

        best = count

        i = k
        while i < len(s):
            if s[i] in vowels:
                count += 1

            if s[i - k] in vowels:
                count -= 1

            if count > best:
                best = count

            i +=1

        return best


        