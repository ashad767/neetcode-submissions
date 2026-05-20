class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = re.sub("[^a-zA-Z0-9]+", "", s).lower()
        left = 0
        right = len(s)-1

        print(s)

        for i in range(0, math.floor(len(s) / 2)):
            if(s[left] != s[right]):
                return False
            if(left >= right):
                break
            left+=1
            right-=1

        return True