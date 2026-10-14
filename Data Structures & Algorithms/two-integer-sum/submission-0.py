class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = []
        for i in range(len(nums)):
            if i <= 0:
                hashmap.append(nums[i])
            elif target-nums[i] in hashmap:
                return [hashmap.index(target-nums[i]), i]
            else:
                hashmap.append(nums[i])