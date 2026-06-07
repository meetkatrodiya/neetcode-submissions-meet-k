class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        mp = {}

        for i in range(0,len(nums)):
            mp[nums[i]] = mp.get(nums[i],0) + 1

        freq_list = [[] for _ in range(len(nums)+1)]

        for key,value in mp.items():
            freq_list[value].append(key)

        result = []

        for i in range(len(freq_list)-1 , 0 ,-1):
            for num in freq_list[i]:
                result.append(num)
                if len(result) == k :
                    return result



