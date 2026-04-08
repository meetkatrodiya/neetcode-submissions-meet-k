class Solution:
    def dailyTemperatures(self, temper: List[int]) -> List[int]:
        ans = [0] * len(temper)
        stack = []

        for i in range(len(temper)):
            while stack and  temper[i] > temper[stack[-1]] :
                prev = stack.pop()
                ans[prev] = i - prev
            stack.append(i)
        
        return ans

