class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_k = 0
        left,right = 0,0
        local_list = []
        while right < len(s):
            while s[right] in local_list:
                local_list.remove(s[left])
                left +=1
            ## Update current window, expand right if violate move left and remove 
            # the letter appear on the left
            local_list.append(s[right])
            max_k = max(max_k,right-left +1)
            right +=1

            

        return max_k



        