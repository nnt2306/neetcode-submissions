class Solution:
    def check_sum(self,arr,start,target):
        end = len(arr)-1
        re_list = []
        while start<end: 
            if arr[start] + arr[end] <target:
                start +=1
            elif arr[start] + arr[end] >target:
                end -=1
            else:
                if [arr[start],arr[end],-target] not in re_list:
                    re_list.append([arr[start],arr[end],-target])
                start +=1
        return re_list

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums_sort = sorted(nums)
        n = len(nums)
        valid_triplet = []
        #glob_valid = None
        for i in range(n):
            if i>=1 and nums_sort[i] == nums_sort[i-1]: # This will skip the things
                continue
            target = -nums_sort[i]
            sum_valid = self.check_sum(nums_sort,i+1,target)
            if sum_valid is not None:
                valid_triplet.extend(sum_valid)
                #glob_valid = sum_valid
        return valid_triplet





        

        