class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count_s = {}

        for char in s:
            if char in count_s:
                count_s[char]+=1
            else:
                count_s[char] =1
        
        for char in t:
            if char not in count_s:
               return False
            else:
                count_s[char] -=1
        
        for key in count_s:
            if count_s[key] != 0:
                return False
        return True
        