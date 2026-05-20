class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []

        for pair in points:
            heapq.heappush_max(heap, (math.sqrt((pair[0]**2) + (pair[1]**2)), pair))
        
        while len(heap) > k:
            heapq.heappop_max(heap)
        
        res = []

        for pair in heap:
            res.append(pair[1])
        
        return res