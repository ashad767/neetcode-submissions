class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mydict = {}

        for word in strs:
            key = []

            for i in range(26):
                key.append(0)

            for i in range(len(word)):
                key[ord(word[i]) - ord('a')] += 1
            
            dict_key = tuple(key)

            if dict_key in mydict:
                mydict[dict_key].append(word)
            else:
                mydict[dict_key] = [word]

        return list(mydict.values())
        