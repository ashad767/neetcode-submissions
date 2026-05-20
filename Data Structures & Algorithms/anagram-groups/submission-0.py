class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mydict = {}
        
        for word in strs:
            key = self.getCount(word)
            if(mydict.get(key) == None):
                mydict[key] = [word]
            else:
                mylist = mydict[key]
                mylist.append(word)
                mydict[key] = mylist

        return mydict.values()

    def getCount(self, s: str) -> int:
        ans = 0
        for i in range(0, len(s)):
            ans += ord(s[i])

        return ans