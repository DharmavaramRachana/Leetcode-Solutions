class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""

        first = strs[0]

        for length in range(len(first), 0, -1):
            prefix = first[:length]
            common = True

            for word in strs[1:]:
                if not word.startswith(prefix):
                    common = False
                    break

            if common:
                return prefix

        return ""
