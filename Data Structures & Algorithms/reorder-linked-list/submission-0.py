# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head.next or not head.next.next:
            return
        

        #split
        slow=fast=head
        while fast.next and fast.next.next:
            slow=slow.next
            fast=fast.next.next
        l2=slow.next
        slow.next=None

        #reverse
        prev=None
        while l2 and l2.next:
            l2next=l2.next
            l2.next=prev
            prev=l2
            l2=l2next
        l2.next=prev

        #merge
        l1=head
        while l1 and l2:
            l1next=l1.next
            l2next=l2.next
            l1.next=l2
            l2.next=l1next
            l1=l1next
            l2=l2next
    





