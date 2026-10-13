class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        m = len(nums)
        count_dict = {}

        for num in nums:
            if num not in count_dict:
                count_dict[num] =1
            else:
                count_dict[num] +=1
        
        for key in count_dict.keys():
            if count_dict[key] > m//2:
                return key

        