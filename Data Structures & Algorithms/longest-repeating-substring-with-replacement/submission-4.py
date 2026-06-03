class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # AABABBBAA, 1
        # ABBBAB, 1
        # ABABA
        
        maxLength = 1
        left = 0
        freqs = defaultdict(int)
        maxf = 0

        for right in range(len(s)):
            freqs[s[right]] += 1
            windowLen = right - left + 1

            # ch = ""
            # mx = 0

            # for key in freqs:
            #     if freqs[key] > mx:
            #         ch = key
            #         mx = freqs[key]

            maxf = max(freqs.values())
            
            while windowLen - maxf > k:
                freqs[s[left]] -= 1
                left += 1
                windowLen -= 1
            maxLength = max(maxLength, right - left + 1)
        
        return maxLength