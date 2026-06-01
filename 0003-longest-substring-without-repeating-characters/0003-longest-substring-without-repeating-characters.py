class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        map_set = {}
        max_length = start = 0

        for i in range(len(s)):
            if s[i] in map_set and start <= map_set[s[i]]:
                start = map_set[s[i]] + 1

            else:
                max_length = max(max_length , i - start + 1)

            map_set[s[i]] = i

        return max_length