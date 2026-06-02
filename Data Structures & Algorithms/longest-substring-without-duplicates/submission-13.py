class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxLength = 0

        # abcabc
        # abcadeafg

        # abcdeddg

        mydict = {}
        left, right = 0, 0

        while right < len(s):
            if s[right] in mydict:
                maxLength = max(maxLength, right - left)

                last = mydict[s[right]]

                print(last)
                if last >= left:
                    left = last + 1
                    while left < len(s) - 1 and s[left] == s[left + 1]:
                        left += 1

                    if left >= right:
                        right = left + 1
                
                    if right >= len(s):
                        break
                    
                    mydict[s[left]] = left

            mydict[s[right]] = right
            right += 1

        print(left, right)
        return max(maxLength, right - left)
 