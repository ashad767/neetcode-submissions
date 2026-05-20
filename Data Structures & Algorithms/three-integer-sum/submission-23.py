class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        answers = set()

        for i in range(len(nums)):
            left = i + 1
            right = len(nums) - 1

            while left < right:
                if nums[left] + nums[right] < -1 * nums[i]:
                    left += 1
                elif nums[left] + nums[right] > -1 * nums[i]:
                    right -= 1
                elif nums[left] + nums[right] == -1 * nums[i]:
                    answers.add((nums[i], nums[left], nums[right]))
                    left += 1
                else:
                    break

        return list(answers)