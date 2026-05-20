class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        my_dict = {}
        counts = defaultdict(int)

        ans = []

        for i in range(len(nums)):
            counts[nums[i]] += 1

        for i in range(1, len(nums) + 1):
            my_dict[i] = []

        for key in counts:
            my_dict[counts[key]].append(key)
        
        for val in list(my_dict.values())[::-1]:
            if len(ans) == k:
                break

            for n in val:
                ans.append(n)

        return ans