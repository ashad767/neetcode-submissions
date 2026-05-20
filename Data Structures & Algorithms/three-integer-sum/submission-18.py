class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        triplets = []

        nums.sort()

        for idx, val in enumerate(nums):
            if idx > 0 and val == nums[idx - 1]:
                continue
            
            left = idx + 1
            right = len(nums) - 1

            while left < right:
                mySum = val + nums[left] + nums[right]
                if mySum > 0:
                    right -= 1
                elif mySum < 0:
                    left +=1
                else:
                    triplets.append([val, nums[left], nums[right]])
                    left += 1
                    while nums[left] == nums[left - 1] and left < right:
                        left += 1

        return triplets