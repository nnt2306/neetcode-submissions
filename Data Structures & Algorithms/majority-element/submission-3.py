class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        candidate_val = nums[0]
        balance_count = 1
        i = 1

        while i < len(nums):
            if balance_count == 0:
                candidate_val = nums[i]
                balance_count = 1
            elif nums[i] == candidate_val:
                balance_count += 1
            else:
                balance_count -= 1

            i += 1

        return candidate_val
                

            
        