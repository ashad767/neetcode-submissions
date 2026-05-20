class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = {}

        for i in range(1, n + 1):
            adj[i] = []
        
        for src, dest, time in times:
            adj[src].append([dest, time])

        shortest = {}

        minHeap = [[0, k]]
        counter = 0
        maxDist = 0

        while minHeap:
            time, node = heapq.heappop(minHeap)

            if node in shortest:
                continue

            shortest[node] = time
            counter += 1
            maxDist = max(maxDist, time)
            
            for dest, time2 in adj[node]:
                if dest not in shortest:
                    heapq.heappush(minHeap, [time + time2, dest])
            
        if counter < n:
            return -1
        
        return maxDist