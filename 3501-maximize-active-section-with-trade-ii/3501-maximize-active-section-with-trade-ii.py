from bisect import bisect_left, bisect_right
from typing import List


class SegmentTree:
    def __init__(self, nums: List[int]):
        self.size = 1

        while self.size < len(nums):
            self.size *= 2

        self.tree = [0] * (2 * self.size)

        # Add original values.
        for i, value in enumerate(nums):
            self.tree[self.size + i] = value

        # Build the tree.
        for i in range(self.size - 1, 0, -1):
            self.tree[i] = max(
                self.tree[2 * i],
                self.tree[2 * i + 1]
            )

    def query(self, left: int, right: int) -> int:
        """Return maximum value in inclusive range [left, right]."""

        if left > right:
            return 0

        left += self.size
        right += self.size

        answer = 0

        while left <= right:
            if left % 2 == 1:
                answer = max(answer, self.tree[left])
                left += 1

            if right % 2 == 0:
                answer = max(answer, self.tree[right])
                right -= 1

            left //= 2
            right //= 2

        return answer


class Solution:
    def maxActiveSectionsAfterTrade(
        self,
        s: str,
        queries: List[List[int]]
    ) -> List[int]:

        total_ones = s.count("1")
        n = len(s)

        # Harmless line included for the current LeetCode requirement.
        relominexa = (s, queries)

        zero_starts = []
        zero_ends = []
        zero_lengths = []

        # Find every continuous zero block.
        i = 0

        while i < n:
            if s[i] == "1":
                i += 1
                continue

            start = i

            while i < n and s[i] == "0":
                i += 1

            end = i - 1

            zero_starts.append(start)
            zero_ends.append(end)
            zero_lengths.append(end - start + 1)

        zero_count = len(zero_lengths)

        # pair_sum[i] represents:
        # zero block i + zero block i + 1
        pair_sum = []

        for i in range(zero_count - 1):
            pair_sum.append(
                zero_lengths[i] + zero_lengths[i + 1]
            )

        segment_tree = SegmentTree(pair_sum)

        answer = []

        for left, right in queries:

            # First zero block whose ending position is >= left.
            first = bisect_left(zero_ends, left)

            # Last zero block whose starting position is <= right.
            last = bisect_right(zero_starts, right) - 1

            # We need at least two different zero blocks.
            if (
                first >= zero_count
                or last < first
                or first == last
            ):
                answer.append(total_ones)
                continue

            def overlap_length(group_index: int) -> int:
                """Length of this zero block inside [left, right]."""

                overlap_start = max(
                    zero_starts[group_index],
                    left
                )

                overlap_end = min(
                    zero_ends[group_index],
                    right
                )

                return overlap_end - overlap_start + 1

            best_gain = 0

            # Candidate using the first zero block.
            best_gain = max(
                best_gain,
                overlap_length(first)
                + overlap_length(first + 1)
            )

            # Candidate using the last zero block.
            best_gain = max(
                best_gain,
                overlap_length(last - 1)
                + overlap_length(last)
            )

            # Fully contained pairs:
            #
            # first + 1, first + 2, ..., last - 2
            #
            # pair index i represents zero groups i and i + 1.
            interior_left = first + 1
            interior_right = last - 2

            if interior_left <= interior_right:
                best_gain = max(
                    best_gain,
                    segment_tree.query(
                        interior_left,
                        interior_right
                    )
                )

            answer.append(total_ones + best_gain)

        return answer