# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = head 
        fast = head
        while fast and fast.next is not None:
            fast = fast.next.next
            slow = slow.next
        
        ## Reverse the second half
        ## Here one problem is that when we do fast and slow pointer we can have a situation like
        # 2 to 4 to 6, and then for reverse this is 8 6 None, this can create infinite loop 
        # when 6 can point to it self and never close while loop

        # So to resolve it we need to do something like 2 to 4 to 6 to None and only 8 to None
        # before reversing, this force not reusing the same middle node from both sides
        prev = None
        second = slow.next
        slow.next = None

        ## Here we need to somehow 
        while second is not None:
            second_next = second.next
            second.next = prev
            prev = second
            second = second_next
        
        curr = head
        while prev is not None:
            tmp1 = curr.next
            tmp2 = prev.next
            
            curr.next = prev
            prev.next = tmp1

            curr = tmp1
            prev = tmp2
        


             


        