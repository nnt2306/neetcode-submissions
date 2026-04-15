# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        curr1,curr2 = list1,list2  #start at front
        dummy = ListNode() # Create a link list at front at first dummy point to None
        tail  = dummy # tail move as ListNode grow
        while curr1 is not None and curr2 is not None:
            if curr1.val <= curr2.val:
                tail.next = curr1
                curr1 = curr1.next
            else:
                tail.next = curr2
                curr2 = curr2.next
            tail = tail.next
        ## We need this step because we need to point to last point, because we do not
        # know surely which node is exhausted first
        if curr1 is not None:
            tail.next = curr1
        else:
            tail.next = curr2

        return dummy.next # Next give another node object, when we have access to the head of 
        # list this will return the whole link list
        