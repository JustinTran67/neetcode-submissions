class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # brute force: sort array and compare the back O(nlogn) naive!
        # use max_heap instead, getting the largest element instantly O(1)
        # time: , space:
        heapq.heapify_max(stones) # create max heap with given stones array
        first = heapq.heappop_max(stones)
        second = None
        while(len(stones) > 0):
            second = heapq.heappop_max(stones)
            heapq.heappush_max(stones, max(first, second) - min(first, second))
            first = heapq.heappop_max(stones)
        return first