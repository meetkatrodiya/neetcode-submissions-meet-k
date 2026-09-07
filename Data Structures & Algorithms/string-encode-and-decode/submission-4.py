class Solution:

    def encode(self, strs: List[str]) -> str:
        if strs == []:
            return ""
        result = ""
        for i in range(0,len(strs)):
            result = result +  str(len(strs[i])) + "#" + strs[i] 
        
        print(result)
        return result
        # encoded_str = 5#hello5#world
    def decode(self, s: str) -> List[str]:
        if s == "":
            return []
        result = [] 
        i = 0
        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            length = int(s[i:j])
            i = j + 1
            j = i + length
            result.append(s[i:j])
            i = j

        return result           




