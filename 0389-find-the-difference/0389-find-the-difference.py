class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        count = {}

        for ch in s:
            count[ch] = 1 + count.get(ch, 0)

        for ch in t:
            if ch not in count or count[ch] == 0:
                return ch

            count[ch] -= 1