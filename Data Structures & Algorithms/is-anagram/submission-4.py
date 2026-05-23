class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False

        mp_s = {}
        mp_t = {}

        for i in range(0,len(s)):
            mp_s[s[i]] = mp_s.get(s[i] , 0) +  1
        
        for j in range(0,len(t)):
            mp_t[t[j]] = mp_t.get(t[j] , 0) + 1

        for key,value in mp_s.items():
            if mp_t.get(key , 0) != value:
                return False
        
        return True