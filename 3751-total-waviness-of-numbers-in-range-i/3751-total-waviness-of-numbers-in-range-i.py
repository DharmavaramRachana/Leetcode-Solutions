class Solution:
    def Waviness(self, num: int) -> int:
        s = str(num)
        cnt = 0

        for i in range(1, len(s) - 1):
            if ((s[i] > s[i-1] and s[i] > s[i+1]) or
                (s[i] < s[i-1] and s[i] < s[i +1])):
                cnt += 1

        return cnt

    def totalWaviness(self, num1: int, num2: int) -> int:
        ans = 0

        for num in range(num1, num2+1):
            ans += self.Waviness(num)

        return ans

        
        