class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)

        triplets = []

        for i in range(len(nums)):

            left = i + 1
            right = len(nums) - 1
            target = -1 * nums[i]

            while left < right:
                mySum = nums[left] + nums[right]
                if(mySum < target):
                    left += 1
                elif(mySum > target):
                    right -=1
                else:
                    ans = [nums[i], nums[left], nums[right]]
                    if(ans not in triplets):
                        triplets.append(ans)
                    left += 1

        return triplets