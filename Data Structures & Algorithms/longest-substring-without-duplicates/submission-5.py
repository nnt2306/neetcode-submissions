class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_k = 0
        left,right = 0,0
        ## Using set will be better of constant look up
        local_set = set()
        while right < len(s):
            while s[right] in local_set:
                local_set.remove(s[left])
                left +=1
            ## Update current window, expand right if violate move left and remove 
            # the letter appear on the left
            local_set.add(s[right])
            max_k = max(max_k,right-left +1)
            right +=1

            

        return max_k



        