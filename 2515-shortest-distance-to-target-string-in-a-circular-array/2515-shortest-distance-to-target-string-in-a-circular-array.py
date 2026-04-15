class Solution:
    def closestTarget(self, words: List[str], target: str, startIndex: int) -> int:
        n = len(words)
        ans = float("inf")

        for i in range(n):
            if words[i] == target:
                forward = (i - startIndex + n) % n
                backward = (startIndex - i + n) % n
                ans = min(ans, forward, backward)

        return -1 if ans == float("inf") else ans