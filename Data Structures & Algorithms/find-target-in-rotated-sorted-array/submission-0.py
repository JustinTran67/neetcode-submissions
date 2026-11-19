class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # naive/brute force solution: one linear pass over nums and return the index of target, if no target -> -1. O(n) solution:
        # proposed solution: Binary search over the array nums to divide the work in half on each iteration: O(logn). Use binary search to find the cut between the sorted end moved to the left and the smaller elements sorted on the right. You should find a pivot index from the first binary search, Then run binary search on the section that contains the target based on what pivot returns, else return -1. Total complexity should be O(logn)

        l, r, m = 0, len(nums) - 1, 0

        while l <= r:
            m = (l + r) // 2
            if target == nums[m]:
                return m
            # left sorted portion
            if nums[l] <= nums[m]:
                if target > nums[m] or target < nums[l]: # search right
                    l = m + 1
                else: # (> nums[l] and < nums[m]) -> search left
                    r = m - 1
            # right sorted portion
            else:
                if target < nums[m] or target > nums[r]: # search left
                    r = m - 1
                else: # (< nums[r] and > nums[m]) -> search right
                    l = m + 1

        return -1
        # time: O(logn), space: O(1)



