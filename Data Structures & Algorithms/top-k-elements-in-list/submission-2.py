class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        mp = {}

        for i in range(0,len(nums)):
            mp[nums[i]] = mp.get(nums[i],0) + 1

        mp_list = [] 

        for key ,value in mp.items():
            mp_list.append([value,key])
        
        mp_list.sort()
        result = []
        for i in range(0,k):
            result.append(mp_list.pop()[1])
        
        return result