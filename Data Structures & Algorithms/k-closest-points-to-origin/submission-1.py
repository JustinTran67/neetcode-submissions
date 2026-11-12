class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # more optimal keeping size of MAXHEAP k
        maxHeap = [] # memory O(n) + O(n) = O(n)
        res = []
        
        for x, y in points:
            dist = math.sqrt(((x - 0) ** 2) + ((y - 0) ** 2))
            heapq.heappush_max(maxHeap, [dist, x, y])
            if len(maxHeap) > k:
                heapq.heappop_max(maxHeap)

        for i in range(k):
            dist, x, y = heapq.heappop_max(maxHeap)
            res.append([x, y])
        
        return res