class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        seenA = set()
        seenB = set()
        common = 0
        ans = []

        for i in range(len(A)):
            seenA.add(A[i])
            seenB.add(B[i])

            if A[i] in seenB:
                common += 1

            if B[i] in seenA and B[i] != A[i]:
                common += 1

            ans.append(common)

        return ans