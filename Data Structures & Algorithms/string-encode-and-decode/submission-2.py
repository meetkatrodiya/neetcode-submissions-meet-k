class Solution:

    def encode(self, strs: List[str]) -> str:
        if strs == [] :
            return ""
        result = ""
        for i in range(0,len(strs)):
            result += str(len(strs[i])) + "#" + strs[i]
        return result

        
        # encoded_str = 5#hello5#world
    def decode(self, s: str) -> List[str]:
        if s == "":
            return []
        result = []
        i = 0 
        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            len_str = int(s[i:j])
            start = j+1
            end = start + len_str
            result.append(s[start:end])
            i = end
        return result


