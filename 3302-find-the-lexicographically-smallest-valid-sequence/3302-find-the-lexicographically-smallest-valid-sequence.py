class Solution:
    def validSequence(self, word1: str, word2: str) -> List[int]:
        n = len(word1)
        m = len(word2)

        if m > n:
            return []

        # last[j] = index in word1 used when matching
        # word2[j:] greedily from the right
        last = [-1] * m

        i = n - 1
        j = m - 1

        while i >= 0 and j >= 0:
            if word1[i] == word2[j]:
                last[j] = i
                j -= 1
            i -= 1

        ans = []
        j = 0
        mismatch_used = False

        for i in range(n):

            # Already completed word2
            if j == m:
                break

            # Case 1: exact match
            if word1[i] == word2[j]:
                ans.append(i)
                j += 1

            # Case 2: use our one mismatch
            elif not mismatch_used:

                # If this is the final char of word2,
                # we can always use the mismatch.
                if j == m - 1:
                    ans.append(i)
                    j += 1
                    mismatch_used = True

                # Otherwise, make sure the remaining
                # word2 can be matched after index i
                elif last[j + 1] > i:
                    ans.append(i)
                    j += 1
                    mismatch_used = True

        if j == m:
            return ans

        return []