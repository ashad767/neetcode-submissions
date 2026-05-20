class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = 1

        while(left < len(numbers) - 1):
            if(numbers[left + 1] == numbers[left]):
                left+=1
                right = left + 1
            elif(numbers[left] + numbers[right] > target):
                left+=1
                right = left + 1
            elif(numbers[left] + numbers[right] < target):
                right+=1
                if(right > len(numbers) - 1):
                    left+=1
                    right = left + 1
            else:
                return [left + 1, right + 1] 