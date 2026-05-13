class Solution:
    def minMoves(self, nums: List[int], limit: int) -> int:
        n = len(nums)
        diff = [0] * (2 * limit + 2)

        for i in range(n // 2):
            a = nums[i]
            b = nums[n - 1 - i]

            low = 1 + min(a, b)
            high = limit + max(a, b)
            s = a + b

            # start with 2 moves for every sum
            diff[2] += 2
            diff[low] -= 1      # 1 move starts
            diff[s] -= 1        # 0 moves at exact sum
            diff[s + 1] += 1    # back to 1 move
            diff[high + 1] += 1 # back to 2 moves

        ans = float('inf')
        moves = 0

        for target in range(2, 2 * limit + 1):
            moves += diff[target]
            ans = min(ans, moves)

        return ans