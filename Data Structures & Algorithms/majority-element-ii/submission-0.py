class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        res = []
        candidate1, candidate2 = None, None
        count1, count2 = 0, 0

        # Step 1: Find candidates
        for num in nums:
            if num == candidate1:
                count1 += 1
            elif num == candidate2:
                count2 += 1
            elif count1 == 0:
                candidate1 = num
                count1 = 1
            elif count2 == 0:
                candidate2 = num
                count2 = 1
            else:
                count1 -= 1
                count2 -= 1

        # Step 2: Verify
        counter1 = sum(1 for x in nums if x == candidate1)
        counter2 = sum(1 for x in nums if x == candidate2)

        if counter1 > len(nums)//3:
            res.append(candidate1)
        if candidate2 != candidate1 and counter2 > len(nums)//3:
            res.append(candidate2)

        return res