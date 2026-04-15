class Solution:
    def _mult_ele(self,nums):
        product = 1 
        for num in nums:
            product *= num
        return product
    
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod_except_self  = []
        for i,num in enumerate(nums):
            left_prod = nums[:i]
            right_prod = nums[i+1:]

            if i==0: 
                left_prod = [1]
            if i == len(nums)-1:
                right_prod = [1]

            prod = self._mult_ele(left_prod) * self._mult_ele(right_prod)
            prod_except_self.append(prod)
        return prod_except_self


        