class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # naive solution is to sort the array O(nlogn) then returning largest at index n - k + 1
        # better solution, use a heap, specifically a minheap that stays size k so we can instantly return the kth larges in O(1) time
        # iterate through nums and heappush into a new heap with size capped at k
        # if size exceeds k then pop off the min element, keeping the kth largest at the
        # root of the heap

        minHeap = []
        for i in nums:
            heapq.heappush(minHeap, i)
            if len(minHeap) > k:
                heapq.heappop(minHeap)
                
        return minHeap[0]