class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], src: int) -> Dict[int, int]:
        adj = {}

        for i in range(n):
            adj[i] = []
        
        for s, d, w in edges:
            adj[s].append([d, w])
        
        minHeap = [[0, src]]

        shortest = {}

        while minHeap:
            w1, v1 = heapq.heappop(minHeap)

            if v1 not in shortest:
                shortest[v1] = w1
            
            for d, w in adj[v1]:
                if d not in shortest:
                    heapq.heappush(minHeap, [w + w1, d])
        
        for i in range(n):
            if i not in shortest:
                shortest[i] = -1
        
        return shortest