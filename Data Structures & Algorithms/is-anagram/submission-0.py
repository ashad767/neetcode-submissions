class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        print(self.getCount(s))
        print(self.getCount(t))
        return self.getCount(s) == self.getCount(t)

    def getCount(self, s: str) -> dict:
        letterCount = {}

        for i in range(0, len(s)):
            if(letterCount.get(s[i]) == None):
                letterCount[s[i]] = 1
            else:
                letterCount[s[i]] = letterCount[s[i]] + 1

        return letterCount