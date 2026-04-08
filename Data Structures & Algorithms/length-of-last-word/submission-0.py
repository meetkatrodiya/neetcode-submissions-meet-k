class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        
        i = len(s) - 1
        first  = -1
        while i >= 0:
            if s[i] != ' ' and first == -1:
                first = i
            elif s[i] == ' ' and first != -1 :
                return first - i 
            i -= 1
        return first + 1