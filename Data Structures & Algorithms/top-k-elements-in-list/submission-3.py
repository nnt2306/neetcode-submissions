class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        '''
          ## One way is to create a hash map and then sorted the value with corresponding keys
        count_dict = {}

        for num in nums:
            if num in count_dict:
                count_dict[num] +=1
            else:
                count_dict[num] = 1
        # .items gives an iterable of (key,value) pair, lambda is one such pair, key = kv[1], to sort
        # based on this value
        sort_list = sorted(count_dict.items(),key = lambda kv:kv[1],reverse = True)
        k_freq = []
        for pair in sort_list:
            if k >0:
                k_freq.append(pair[0])
                k-=1

        return k_freq
        This will create complexity of O(nlogn)
        '''

        ## Better way: WE create a bucket frequency to group all values occur f time 
        count_dict = {}

        for num in nums:
            if num in count_dict:
                count_dict[num] +=1
            else:
                count_dict[num] = 1
        
        # The max frequency is at most length of the input, so we create
        # a list frequency of length n+1
        
        n = len(nums)
        bucket_freq = [[] for _ in range(n+1)]
        for key,freq in count_dict.items():
            bucket_freq[freq].append(key)
           
        k_freq = []
        while n>0 and k>0:
            if bucket_freq[n]: # the list is empty or not then we take the corresponding nb of element
            #from it
                min_ele = min(k,len(bucket_freq[n]))
                k_freq.extend(bucket_freq[n][:min_ele])
                k -= min_ele
            n-=1 # this will go through all elements what ever the list is empty or not
        return k_freq
        
                
            
        




       