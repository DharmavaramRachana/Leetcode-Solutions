class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        need = {}
        available = {}

        for ch in ransomNote:
            need[ch] = 1 + need.get(ch, 0)

        for ch in magazine:
            available[ch] = 1 + available.get(ch, 0)


        for ch, count in need.items():
            if available.get(ch, 0) < count:
                return False

        return True

        