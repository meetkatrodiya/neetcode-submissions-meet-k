class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        for i in range(0,len(nums)):
            left = i + 1
            right = len(nums) - 1
            
            while(left < right):
               
                if nums[i] + nums[left] + nums[right] < 0 or i == left:
                    left += 1
                elif nums[i] + nums[left] + nums[right] > 0 or i == right:
                    right -= 1
                else:
                    if [nums[i],nums[left],nums[right]] not in result:
                        result.append([nums[i],nums[left],nums[right]])
                    left += 1
                    right -= 1
        return result