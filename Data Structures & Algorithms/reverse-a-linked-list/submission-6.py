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
        '''
        head_1 = None ## Still use extra memory for new nodes
        while head is not None:
             head_1 = ListNode(head.val,head_1)
             head = head.next
        return head_1
        '''
        prev = None
        curr = head # curr point to node 0
        ## Example [0,1,2,3]
        while curr is not None: 
            nxt = curr.next # nxt point to node 1
            curr.next = prev # curr next point to prev = None
            prev = curr # Update prev = curr = 0
            curr = nxt # Update curr to 1 then we repeat
        return prev # This wil become a link list curr will become None
             




       



        