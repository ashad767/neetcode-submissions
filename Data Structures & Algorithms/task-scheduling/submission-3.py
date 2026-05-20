class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        heap = []
        freqs = {}

        for task in tasks:
            freqs[task] = freqs[task] + 1 if task in freqs else 1
        
        for key in freqs:
            heapq.heappush_max(heap, (freqs[key], key))
            

        cycles = 0
        cooldowns = {}
        
        while len(heap) > 0 or len(freqs) > 0:
            curr = None

            if len(heap) > 0:
                curr = heapq.heappop_max(heap)
            
            # if curr[1] in cooldowns and cooldowns[curr[1]] > 0:
            #     cycles += 1
                
            #     for cd in cooldowns:
            #         cooldowns[cd] -= 1
                
            #     continue

            
            cycles += 1
            

            for cd in cooldowns:
                cooldowns[cd] -= 1

                if cooldowns[cd] == 0 and cd in freqs:
                    heapq.heappush_max(heap, (freqs[cd], cd))
            
            if curr:
                freqs[curr[1]] -= 1
                if freqs[curr[1]] > 0:
                    cooldowns[curr[1]] = n
                else:
                    freqs.pop(curr[1])
            
            print(cooldowns, freqs, curr)

        return cycles