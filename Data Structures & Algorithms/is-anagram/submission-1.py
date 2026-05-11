class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count_s = {}
        count_t = {}

        for i in s:
            if i in count_s:
                count_s[i] += 1
            else:
                count_s[i] = 1
        for i in t:
            if i in count_t:
                count_t[i] += 1
            else:
                count_t[i] = 1

        if(len(count_s) != len(count_t)):
            return False
        else:
            for i in count_s:
                if i not in count_t:
                    return False
                else:
                    if count_s[i] != count_t[i]:
                        return False
        return True


