class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        triplets = defaultdict(list)
        nums.sort()
        
        zero = 0
        first = 1
        second = 2

        while(zero < len(nums) - 2):
            if(nums[zero] + nums[first] + nums[second] == 0):
                newTriplet = [nums[zero], nums[first], nums[second]]

                if(triplets.get(tuple(newTriplet)) == None):
                    triplets[tuple(newTriplet)] = newTriplet

                # if newTriplet not in triplets:
                #     triplets.append(newTriplet)
                
            second += 1

            if(second == len(nums)):
                first += 1
                second = first + 1

            if(first == len(nums) - 1):
                zero += 1
                first = zero + 1
                second = first + 1

        return list(triplets.values())