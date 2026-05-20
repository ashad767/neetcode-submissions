class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        right = 1

        length = 1

        if len(s) == 0:
            return 0

        chars = {}
        chars[s[left]] = left

        while right < len(s) and left < len(s):            
            if s[right] in chars and left <= chars[s[right]]:
                left = chars[s[right]] + 1
                
                while left < len(s) - 1 and s[left] == s[left + 1]:
                    left += 1
                    right = left + 1

                    if right >= len(s):
                        return length

            #elif s[left] == s[right]:
               # left += 1

            chars[s[right]] = right
            right += 1

            length = max(length, right - left)
        return length