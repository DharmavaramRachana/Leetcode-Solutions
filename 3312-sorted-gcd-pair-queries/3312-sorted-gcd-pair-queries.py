class Solution:
    def gcdValues(self, nums: List[int], queries: List[int]) -> List[int]:
        max_num = max(nums)

        
        frequency = [0] * (max_num + 1)

        for num in nums:
            frequency[num] += 1

        
        exact_gcd = [0] * (max_num + 1)

       
        for gcd_value in range(max_num, 0, -1):
            divisible_count = 0

           
            for multiple in range(gcd_value, max_num + 1, gcd_value):
                divisible_count += frequency[multiple]

            
            pair_count = divisible_count * (divisible_count - 1) // 2

            
            for multiple in range(gcd_value * 2, max_num + 1, gcd_value):
                pair_count -= exact_gcd[multiple]

            exact_gcd[gcd_value] = pair_count

        
        prefix = [0] * (max_num + 1)

        for gcd_value in range(1, max_num + 1):
            prefix[gcd_value] = (
                prefix[gcd_value - 1] + exact_gcd[gcd_value]
            )

        answer = []

        for query in queries:
            
            gcd_value = bisect_right(prefix, query)
            answer.append(gcd_value)

        return answer