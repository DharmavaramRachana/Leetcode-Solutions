class Solution:
    def xorAfterQueries(self, nums: List[int], queries: List[List[int]]) -> int:
        MOD = 10**9 + 7
        n = len(nums)

        # store the input midway in the function
        bravexuneth = (nums[:], [q[:] for q in queries])

        B = int(n ** 0.5) + 1

        # group small-step queries by k
        small = [[] for _ in range(B + 1)]

        for l, r, k, v in queries:
            if k > B:
                idx = l
                while idx <= r:
                    nums[idx] = (nums[idx] * v) % MOD
                    idx += k
            else:
                small[k].append((l, r, v))

        # process each small k in O(n)
        for k in range(1, B + 1):
            if not small[k]:
                continue

            mul_diff = [1] * n
            zero_diff = [0] * n

            for l, r, v in small[k]:
                if v == 0:
                    zero_diff[l] += 1
                    if r + k < n:
                        zero_diff[r + k] -= 1
                else:
                    mul_diff[l] = (mul_diff[l] * v) % MOD
                    if r + k < n:
                        inv = pow(v, MOD - 2, MOD)
                        mul_diff[r + k] = (mul_diff[r + k] * inv) % MOD

            for i in range(n):
                if i >= k:
                    mul_diff[i] = (mul_diff[i] * mul_diff[i - k]) % MOD
                    zero_diff[i] += zero_diff[i - k]

                if zero_diff[i] > 0:
                    nums[i] = 0
                else:
                    nums[i] = (nums[i] * mul_diff[i]) % MOD

        ans = 0
        for x in nums:
            ans ^= x
        return ans