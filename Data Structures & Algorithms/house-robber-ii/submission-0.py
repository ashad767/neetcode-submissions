class Solution:
    def rob(self, nums: List[int]) -> int:
        return max(nums[0], self.get_rob(nums[1:]), self.get_rob(nums[:-1]))


    def get_rob(self, nums) -> int:
        rob1, rob2 = 0, 0

        for n in nums:
            tmp = rob2
            rob2 = max(n + rob1, rob2)
            rob1 = tmp
        
        return rob2