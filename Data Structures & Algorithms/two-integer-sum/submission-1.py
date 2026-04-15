class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        comp_dict = {}
        for index,num in enumerate(nums):
            comp = target-num
            if comp not in comp_dict:
                comp_dict[num] = index
            else:
                return [comp_dict[comp],index] 