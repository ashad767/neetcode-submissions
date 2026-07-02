class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = minRes = maxRes = nums[0]

        for n in nums[1:]:
            if n == 0:
                minRes = maxRes = 1

            tempMin = minRes * n
            tempMax = maxRes * n

            minRes = min(tempMin, tempMax, n)
            maxRes = max(tempMax, tempMin, n)
            
            print(maxRes, minRes)
            res = max(res, maxRes)

        # 2, 4, -3, 5, -1, -1, 3

        return res