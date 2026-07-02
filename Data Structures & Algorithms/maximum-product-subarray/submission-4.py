class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # res = nums[0]
        # maxRes = minRes = 1

        # for n in nums:
        #     if n == 0:
        #         minRes = maxRes = 1

            
        #     tempMin = minRes * n
        #     tempMax = maxRes * n

        #     minRes = min(tempMin, tempMax, n)
        #     maxRes = max(tempMax, tempMin, n)
            
        #     print(maxRes, minRes)
        #     res = max(res, maxRes)

        # # 2, 4, -3, 5, -1, -1, 3

        # return res
        res = nums[0]
        curMin, curMax = nums[0], nums[0]

        for num in nums[1:]:
            tmp = curMax * num
            curMax = max(num * curMax, num * curMin, num)
            curMin = min(tmp, num * curMin, num)
            res = max(res, curMax)

            print(curMax, curMin)
        return res