class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        set_num = set(nums)
        seq_list = []
        for num in set_num:
            if num-1 not in set_num:
                seq_list.append(num)
        if not seq_list:
            return 0
        if len(seq_list) == len(set_num):
            return 1
        ## Here one thing to remeber: when we have already a starting point, we need to be
        ## careful to growing sequence, we should use while instead of for because the set is 
        ## unordered to somehow it can missed the thing
        global_k = 1
        for start_num in seq_list:
            local_k = 1
            current = start_num
            while current +1 in set_num:
                 # This check whether current +1 exist, if yes continue, no stop
        ## Remember when we do a hask look up, python does not look through all elements once by once
        ## Instead this does a constant look up through the hash set (map) with average O(1) and worst is O(n)
                current +=1
                local_k +=1
            global_k = max(global_k,local_k)
        return global_k


        
        
