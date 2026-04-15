class Solution:
    def findMin(self, nums: List[int]) -> int:
        start = 0
        end = len(nums)-1
        

        while start <end : 
            mid = start + (end-start)//2

            if nums[mid] > nums[end]:
                start = mid+1
            else: # Here this will check nums[mid] <= nums[end], we know that the minimum
            ## will be on the right include this mid point, we can not throw it
        
                end = mid
        return nums[start]
                    
                

        