class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash = {}
        for index, value in enumerate(nums):
            if target - value in hash:
                return [hash[target-value], index]
            hash[value] = index