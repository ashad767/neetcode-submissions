class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mydict = {}

        for i in range(len(nums)):
            if target - nums[i] in mydict:
                return [mydict[target - nums[i]], i]
            
            mydict[nums[i]] = i
