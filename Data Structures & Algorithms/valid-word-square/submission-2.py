class Solution:
    def validWordSquare(self, words: List[str]) -> bool:
        for i in range(0 , len(words)):
            for j in range(0, len(words[i])):
                if j < len(words) and i < len(words[j]) :
                    if words[i][j] != words[j][i] :
                        return False
                else :
                    return False
        
        return True 