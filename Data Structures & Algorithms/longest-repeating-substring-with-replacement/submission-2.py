class Solution:
    '''
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
        ## This solution has some flaws, especially in time
        # when we do the max we need to scan all the dicitionary and
        # this can costly
        while right < len(s):
            max_freq= self.max_freq_chr(freq_map,s[right])
            
            while right-left+1 - max_freq >k:
                freq_map[s[left]] -=1
                left +=1
                
            max_k = max(max_k, right-left+1)
            right +=1
        return max_k
    '''
    def characterReplacement(self, s: str, k: int) -> int:

    ## Instead what we do now we will update the max freq each time
    # by maintaing the global variable
            freq_map = {}
            left = 0
            max_k = 0
            max_freq = 0

            for right in range(len(s)):
                freq_map[s[right]] = freq_map.get(s[right], 0) + 1
                max_freq = max(max_freq, freq_map[s[right]])
                
                ## Remember that when the condition of replacing is not satisfied
                # we will shrink the window until it satisfied, along with 
                # it we need to remove the frequency for previous window
                # and continue update for new window
                while right - left + 1 - max_freq > k:
                    freq_map[s[left]] -= 1
                    left += 1

                max_k = max(max_k, right - left + 1)
                right +=1

            return max_k
                        