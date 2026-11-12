class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # distance = math.sqrt(((x1 - x2)**2) + ((y1 - y2)**2))
        # 1. iterate over every point in points and calculate the ditance to origin O(n)
        # put all distances in a list as [distance , [x, y]]
        # 2. create a minheap from the new array of distances O(logn)
        # 3. pop the k closest distances from the minheap O(logn) then append to a final res list
        dist = []
        res = []

        for point in points:
            x, y = point[0], point[1]
            distance = math.sqrt(((x - 0) ** 2) + ((y - 0) ** 2))
            dist.append([distance, [x, y]])
        
        heapq.heapify(dist) # creates minheap comapring dist value at [0] first

        for i in range(k): # O(klogn)
            value = heapq.heappop(dist)
            res.append(value[1])
        
        return res