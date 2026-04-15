class Solution:
    def max_freq_chr(self,require_map,char):
        if char in require_map:
            require_map[char] +=1
        else:
            require_map[char] = 1
        
        return max(require_map.values())

    def characterReplacement(self, s: str, k: int) -> int:
        freq_map = {}
        
        left,right = 0,0
        max_k = 0
        while right < len(s):
            max_freq= self.max_freq_chr(freq_map,s[right])
            
            while right-left+1 - max_freq >k:
                freq_map[s[left]] -=1
                left +=1
                
            max_k = max(max_k, right-left+1)
            right +=1
        return max_k
                