class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        triplets = []
        nums.sort()
        
        zero = 0
        first = 1
        second = 2

        # [-4, -1, -1, 0, 1, 2]

        while(zero < len(nums) - 2):
            if(nums[zero] > 0):
                break
            if(first >= len(nums) - 1 or (zero > 0 and nums[zero] == nums[zero - 1])):
                zero += 1
                first = zero + 1
                second = first + 1
                continue
            if(second >= len(nums) or (nums[first] == nums[first - 1] and first - 1 != zero)):
                first += 1
                second = first + 1
                continue
            if(nums[second] == nums[second - 1] and second - 1 != first):
                second += 1
                continue

            if(nums[zero] + nums[first] + nums[second] == 0):
                # newTriplet = [nums[zero], nums[first], nums[second]]
                triplets.append([nums[zero], nums[first], nums[second]])

                # if(triplets.get(tuple(newTriplet)) == None):
                #     triplets[tuple(newTriplet)] = newTriplet
                
            second += 1

        return triplets