class Solution:
    def rob(self, nums: List[int]) -> int:
        monies = [0] * (len(nums) + 1)
        monies[1] = nums[0]

        for i in range(2, len(nums) + 1):
            monies[i] += max(monies[i-2] + nums[i-1], monies[i-1])
        
        # print(monies)
        return monies[len(monies)-1]