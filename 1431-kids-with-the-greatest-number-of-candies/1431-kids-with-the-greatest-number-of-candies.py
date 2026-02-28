class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        n = len(candies)
        max_c = candies[0]

        i = 1

        while i < n:
            if candies[i] > max_c:
                max_c = candies[i]

            i += 1

        
        result = []
        i = 0

        while i < n:
            if candies[i] + extraCandies >= max_c:
                result.append(True)

            else:
                result.append(False)

            i += 1

        return result
