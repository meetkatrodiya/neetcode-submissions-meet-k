class Solution:
    def isPalindrome(self, s: str) -> bool:
        s.replace(" ","")
        s = s.lower()
        trim_str = ""
        for i in range(0, len(s)):
            if s[i].isalnum():
                trim_str += s[i]


        print(trim_str)

        for i in range(0,len(trim_str)):
            if trim_str[i] != trim_str[len(trim_str)-i-1] :
                return False
        
        return True
        