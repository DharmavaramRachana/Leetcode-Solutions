class Solution:
    def minimumPushes(self, word: str) -> int:
        frequencies = Counter(word)

        # Most frequent letters first
        counts = sorted(frequencies.values(), reverse=True)

        total_pushes = 0

        for i, frequency in enumerate(counts):
            pushes_per_letter = (i // 8) + 1
            total_pushes += frequency * pushes_per_letter

        return total_pushes