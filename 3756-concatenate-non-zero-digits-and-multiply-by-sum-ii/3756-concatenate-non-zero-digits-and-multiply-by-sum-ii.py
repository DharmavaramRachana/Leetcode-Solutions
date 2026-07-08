class Solution:
    def sumAndMultiply(self, s: str, queries: List[List[int]]) -> List[int]:
        MOD = 10**9 + 7
        m = len(s)

        cnt = [0] * (m + 1)      
        sm = [0] * (m + 1)       

        vals = [0]               
        pow10 = [1] * (m + 1)

        for i in range(m):
            pow10[i + 1] = (pow10[i] * 10) % MOD

        for i, ch in enumerate(s):
            d = int(ch)
            cnt[i + 1] = cnt[i]
            sm[i + 1] = sm[i]

            if d != 0:
                cnt[i + 1] += 1
                sm[i + 1] += d
                vals.append((vals[-1] * 10 + d) % MOD)

        ans = []

        for l, r in queries:
            left_count = cnt[l]
            right_count = cnt[r + 1]

            length = right_count - left_count
            digit_sum = sm[r + 1] - sm[l]

            x = (vals[right_count] - vals[left_count] * pow10[length]) % MOD

            ans.append((x * digit_sum) % MOD)

        return ans