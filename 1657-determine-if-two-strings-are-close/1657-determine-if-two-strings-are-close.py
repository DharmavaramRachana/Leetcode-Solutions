class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2):
            return False

        freq1 = {}
        freq2 = {}

        for ch in word1:
            freq1[ch] = 1 + freq1.get(ch, 0)

        for ch in word2:
            freq2[ch] = 1 + freq2.get(ch, 0)

        if set(freq1.keys()) != set(freq2.keys()):
            return False

        countMap = {}

        for val in freq1.values():
            countMap[val] = 1 + countMap.get(val, 0)

        for val in freq2.values():
            if val not in countMap:
                return False

            countMap[val] -= 1
            if countMap[val] < 0:
                return False

        return True


        