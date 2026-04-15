class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
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