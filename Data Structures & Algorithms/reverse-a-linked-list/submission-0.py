# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        ## Naive way to solve
        ll_array = []
        current =head
        while current is not None:
            ll_array.append(current.val)
            current = current.next
        n = len(ll_array)
        idx = 0
        head1 = None
        
        while idx < len(ll_array):
            head1 = ListNode(ll_array[idx],head1)
            idx +=1
          
        return head1

       



        