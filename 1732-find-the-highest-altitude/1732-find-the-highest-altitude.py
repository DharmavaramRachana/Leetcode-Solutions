class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        prefix = 0
        i = 0
        best = 0

        while i < len(gain):
            prefix += gain[i]

            if prefix > best:
                best = prefix
            
            i += 1

        return best