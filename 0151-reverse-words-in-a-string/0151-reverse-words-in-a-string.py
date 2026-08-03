class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split()

        result = ""

        for word in words:
            if result:
              result = word + " " + result

            else:
                result = word

        return result
        