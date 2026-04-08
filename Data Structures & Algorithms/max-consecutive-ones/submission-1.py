class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_count = 0 
        count = 0
        if nums[0] == 1 :
            count += 1
        
        for i in range(1,len(nums)):
            if nums[i] == 1 and nums[i-1] == 1 :
                count += 1
            elif nums[i] == 1 and nums[i-1] == 0 :
                count = 1
            else :
                if count > max_count :
                    max_count = count
                count = 0 
        max_count = max(count,max_count)
        return max_count