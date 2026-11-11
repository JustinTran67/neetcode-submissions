class KthLargest:

    def __init__(self, k: int, nums: List[int]): # min heap of size k getting the top is the kth largest and is O(1) lookup
        self.minHeap, self.k = nums, k
        heapq.heapify(self.minHeap) # special function for creating minHeap
        while len(self.minHeap) > k:
            heapq.heappop(self.minHeap)

    def add(self, val: int) -> int:
        heapq.heappush(self.minHeap, val)
        if len(self.minHeap) > self.k:
            heapq.heappop(self.minHeap)
        return self.minHeap[0]