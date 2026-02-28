class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        freq = {}

        for num in arr:
            if num in freq:
                freq[num] +=1
            else:
                freq[num]= 1


        seen = set()
        for count in freq.values():
            if count in seen:
                return False

            seen.add(count)

        return True