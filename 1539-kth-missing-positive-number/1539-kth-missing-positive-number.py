class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        i = 0
        num = 1

        
        while k > 0:
            if i < len(arr) and arr[i] == num:
                i += 1
            else:
                k -= 1

            num += 1

        return num - 1