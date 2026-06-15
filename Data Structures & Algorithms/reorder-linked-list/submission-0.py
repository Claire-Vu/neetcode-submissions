# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # We are given just the head
        # Need to find the tail pointer
        # Point tail.next to head.next.next
        # Point head.next to tail

        # New head becomes tail.next 
        # repeat the reorderList(tail.next)

        # When to stop? when tail.next is None

        # Finding the tail pointer
        if (head == None or head.next == None):
            return
        else:
            tail = head.next
            follower_tail = tail
            while (tail.next != None):
                follower_tail = tail
                tail = tail.next
            tail.next = head.next
            head.next = tail
            # Discard the previous node pointing to our tail
            follower_tail.next = None

            # Repeat the pattern with the rest of the linked list
            self.reorderList(tail.next)

        