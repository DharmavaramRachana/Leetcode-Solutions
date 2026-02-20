class Solution:
    def makeLargestSpecial(self, s: str) -> str:
        parts = []
        bal = 0
        start = 0

        for i, ch in enumerate(s):
            bal += 1 if ch == '1' else -1
            if bal == 0:
                # s[start:i+1] is a top-level special substring: 1 + inner + 0
                inner = s[start + 1:i]
                best_inner = self.makeLargestSpecial(inner)  # recurse
                parts.append("1" + best_inner + "0")
                start = i + 1

        # reorder top-level parts for maximum lexicographic result
        parts.sort(reverse=True)
        return "".join(parts)
        