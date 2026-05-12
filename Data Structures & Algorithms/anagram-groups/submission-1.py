class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = []
        j = 1

        #for i in strs:
        while len(strs) > 0:
            i = strs[0]
            curr = sorted(i)
            temp = []
            temp.append(i)
            for k in range(j,len(strs)):
                nextt = sorted(strs[k])
                if curr == nextt:
                    temp.append(strs[k])
            ans.append(temp)
            for word in temp:
                strs.remove(word)
        
        return ans