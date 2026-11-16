class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # naive/brute force appraoch: would be to iterate over all combinations of CPU cycles and find the minimum given the repeat task cooldown, O(n^2) or worse.
        # proposed solution: store the frequencies of each task in an array/hashmap. greedily process the most frequent task first by using a maxheap to always get the most frequent task at any given time. init a variable "time" to keep track if the cooldown period.
        time = 0 
        freq = collections.defaultdict(int) # start at 0 so we can increment: O(26) -> O(1)
        q = collections.deque([]) # (freq, time after cooldown period) O(26) -> O(1)

        for i in tasks: # O(n)
            freq[i] += 1

        maxHeap = list(freq.values()) # O(26) -> O(1)
        heapq.heapify_max(maxHeap)

        while maxHeap or q: # O(n) heap and queue hold at most the number of elements in tasks if all unique
            time += 1 # increment the time for this process
            if maxHeap:
                process = heapq.heappop_max(maxHeap) # get the process: O(log26) -> O(1)
                if process > 1:
                    q.append((process - 1, time + n)) # add process into the queue for cooldown
            if q:
                p, t = q[0]
                if time == t: # if cooldown is up for the queued process -> add back to heap
                    q.popleft()
                    heapq.heappush_max(maxHeap, p) # O(log26) -> O(1)
        
        return time

        # time: O(n), space: O(1)
            




