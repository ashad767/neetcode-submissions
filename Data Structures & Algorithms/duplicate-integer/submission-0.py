class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        myList = {}

        for i in range(0, len(nums)):
            if(myList.get(nums[i]) != None):
                return True
            myList[nums[i]] = i

        return False 