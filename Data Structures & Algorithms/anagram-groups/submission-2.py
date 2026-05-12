class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = {}

        for i in strs:
            sorted_word = ''.join(sorted(i))
            if sorted_word not in ans:
                ans[sorted_word] = []
                ans[sorted_word].append(i)
            else :
                ans[sorted_word].append(i)
        return list(ans.values())