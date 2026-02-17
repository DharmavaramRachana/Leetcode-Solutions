class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        i = len(s) - 1
        length = 0

        while i >=0 and s[i] == " ": # in order to skip the trailing spaces after that we move to another loop 
            i -= 1


        while i >= 0 and s[i] != " ":
            length += 1
            i -= 1

        return length
        