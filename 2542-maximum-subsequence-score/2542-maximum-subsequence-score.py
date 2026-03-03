class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        total = res = 0
        heap = []
        pairs = zip(nums1, nums2)

        sorted_pairs = sorted(pairs, key = lambda x: x[1], reverse = True)

        for pair in sorted_pairs:
            num1, num2 = pair

            heapq.heappush(heap, num1)
            total += num1


            if len(heap) > k:
                total -= heapq.heappop(heap)

            if len(heap) == k:
                res = max(res, total * num2)

        return res
         