class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        minheap = nums
        heapq.heapify(minheap)

        while len(minheap) > k:
            heapq.heappop(minheap)

        return minheap[0]