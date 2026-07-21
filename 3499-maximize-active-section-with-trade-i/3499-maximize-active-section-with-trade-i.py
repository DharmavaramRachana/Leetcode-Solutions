class Solution:
    def maxActiveSectionsAfterTrade(self, s: str) -> int:
        t = "1" + s + "1"
        groups = []

        i = 0

        while i < len(t):
            char = t[i]
            length = 0

            while i < len(t) and t[i] == char:
                length += 1
                i += 1

            groups.append((char, length))

        max_gain = 0

       
        for i in range(1, len(groups) - 1):
            if (
                groups[i][0] == "1"
                and groups[i - 1][0] == "0"
                and groups[i + 1][0] == "0"
            ):
                gain = groups[i - 1][1] + groups[i + 1][1]
                max_gain = max(max_gain, gain)

        return s.count("1") + max_gain