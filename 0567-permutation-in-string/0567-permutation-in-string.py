class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        count, window = [0] * 26, [0] * 26

        for char in s1:
            count[ord(char) - ord("a")] += 1

        for i in range(len(s1)):
            window[ord(s2[i]) - ord("a")] += 1

        if count == window:
            return True

        for i in range(len(s1), len(s2)):
            window[ord(s2[i]) - ord("a")] += 1

            window[ord(s2[i - len(s1)]) - ord("a")] -= 1

            if count == window:
                return True

        return False