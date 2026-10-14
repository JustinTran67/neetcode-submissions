class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        ha = {}
        for i in range(len(numbers)):
            diff = target - numbers[i]
            if diff in ha:
                return [ha[diff], i + 1]
            else:
                ha[numbers[i]] = i + 1