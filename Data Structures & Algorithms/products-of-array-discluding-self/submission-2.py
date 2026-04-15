class Solution:
    def _mult_ele(self,nums):
        product = 1 
        for num in nums:
            product *= num
        return product
    
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ## First way: we create a sub function that multiply left and right at the index
        ## This will have O(n^2) time complexity
        '''
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

        '''

        # Second way: To get O(n) time complexity, instead of doing repetitively compute at chosen
        # index, we compute it using one forward loop and one backward loop
        left_list = [1]
        right_list = [1]
        prod_list = []
        n = len(nums)
        left_prod = right_prod = 1
        
        for i in range(n-1):
            left_prod *= nums[i]
            right_prod *= nums[n-1-i]
            left_list.append(left_prod)
            right_list.append(right_prod)
        
        
        for i in range(n):
            prod_list.append(left_list[i]*right_list[n-1-i])
        return prod_list
        
        


        

        