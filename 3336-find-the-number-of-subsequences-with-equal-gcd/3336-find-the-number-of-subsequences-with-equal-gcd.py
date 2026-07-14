class Solution:
    def subsequencePairCount(self, nums: List[int]) -> int:
        MOD = 10**9 + 7
        max_num = max(nums)

        
        dp = [[0] * (max_num + 1) for _ in range(max_num + 1)]
        dp[0][0] = 1

        for num in nums:
            new_dp = [row[:] for row in dp]

            for gcd1 in range(max_num + 1):
                for gcd2 in range(max_num + 1):
                    ways = dp[gcd1][gcd2]

                    if ways == 0:
                        continue

                    # Add num to seq1
                    new_gcd1 = gcd(gcd1, num)
                    new_dp[new_gcd1][gcd2] = (
                        new_dp[new_gcd1][gcd2] + ways
                    ) % MOD

                    # Add num to seq2
                    new_gcd2 = gcd(gcd2, num)
                    new_dp[gcd1][new_gcd2] = (
                        new_dp[gcd1][new_gcd2] + ways
                    ) % MOD

            dp = new_dp

        answer = 0

        
        for common_gcd in range(1, max_num + 1):
            answer = (answer + dp[common_gcd][common_gcd]) % MOD

        return answer