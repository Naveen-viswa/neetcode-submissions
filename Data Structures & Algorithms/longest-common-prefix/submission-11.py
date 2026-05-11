class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = strs[0]
        empty = ""
        if len(prefix) == 0 : return empty

        for i in range(1,len(strs)):

            match = bool() 

            if len(strs[i]) == 0 : return empty

            iter = min(len(strs[i]), len(prefix))

            word = strs[i]

            

            for j in range(0, iter):
                
                if prefix[j] == word[j] : match = True
                else :
                    match = False
                    prefix = prefix[:j]
                    break
            if match == True : prefix = prefix[:iter]
        
        return prefix


