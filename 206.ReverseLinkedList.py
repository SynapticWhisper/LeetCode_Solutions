from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        next_val = None
        while head:
            new_node = ListNode(val=head.val, next=next_val)
            head = head.next
            next_val = new_node
        return next_val