class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned = ""

        for char in s:
            if char.isalnum():
                cleaned += char.lower()

        reversed_string = cleaned[::-1]

        return cleaned == reversed_string

            
        









    
        