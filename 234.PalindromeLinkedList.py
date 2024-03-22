from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val: int = val
        self.next: Optional[ListNode] = next


class Solution:
    def isPalindrome_1(self, head: Optional[ListNode]) -> bool:
        fast, slow, prev = head, head, None

        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        
        if fast.next:
            slow = slow.next

        while slow:
            next_val = slow.next
            slow.next = prev
            prev = slow
            slow = next_val

        while prev:
            if prev.val != head.val:
                return False
            prev = prev.next
            head = head.next
        return True
    
    def isPalindrome_2(self, head: Optional[ListNode]) -> bool:
        l = []
        while head:
            l.append(head.val)
            head = head.next
        
        j = len(l) - 1
        
        for i in range(len(l)):
            if l[j-i] != l[i]:
                return False
        return True
    
if __name__ == "__main__":
    node = ListNode(1, ListNode(2))
    Solution().isPalindrome_3(node)