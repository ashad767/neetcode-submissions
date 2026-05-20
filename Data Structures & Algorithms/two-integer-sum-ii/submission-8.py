class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = 1

        while left < len(numbers) - 1:
            num = target - numbers[left]
            
            if numbers[len(numbers) - 1] < num:
                left += 1
                right = left + 1
                continue
            
            if numbers[right] > num:
                left += 1
                right = left + 1
                continue

            if numbers[left] + numbers[right] == target:
                return [left + 1, right + 1]

            if right == len(numbers) - 1:
                left += 1
                right = left + 1
            else:
                right += 1