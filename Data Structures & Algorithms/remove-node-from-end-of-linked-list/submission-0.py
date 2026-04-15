# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(-1) # Create a link list at front at first dummy point to None
        first = dummy
        second = dummy
        dummy.next = head

        for _ in range(n):
            second = second.next
            if second is None:
                return head

        while second is not None and second.next is not None:
            print(first.val)
            first = first.next
            print(first.val)
            print(second.val)
            second = second.next

        
        first.next = first.next.next
        second.next = None

        return dummy.next

        
        


        