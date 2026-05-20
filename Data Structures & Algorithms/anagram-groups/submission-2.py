class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        myDict = defaultdict(list)

        for word in strs:
            numWords = self.getCount(word)

            myDict[numWords].append(word)


        return myDict.values()

    def getCount(self, s: str) -> tuple:
        letterCount = [0] * 26

        for i in range(0, len(s)):
            val = ord(s[i]) - 97
            letterCount[val] = letterCount[val] + 1

        return tuple(letterCount)