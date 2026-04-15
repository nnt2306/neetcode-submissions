# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        '''
        ## Naive way to solve by creating a new array to store 

        ll_array = [] ## Create extra space by creating an array
        while head is not None:
            ll_array.append(head.val)
            head= head.next
        n = len(ll_array)
        idx = 0
        head1 = None
        
        while idx < len(ll_array):
            head1 = ListNode(ll_array[idx],head1)
            idx +=1
          
        return head1
        '''
        head_1 = None
        ## Better way without extra memory
        while head is not None:
             head_1 = ListNode(head.val,head_1)
             head = head.next
        return head_1


       



        