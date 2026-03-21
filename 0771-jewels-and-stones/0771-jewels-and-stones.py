class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        seen = set(jewels)
        res = 0

        for i in range(len(stones)):
            if stones[i] in seen:
                res += 1

            i += 1

        return res
            
        