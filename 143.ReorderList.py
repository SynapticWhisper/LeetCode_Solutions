from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        cache: dict = {}
        temp = head
        counter = 0
        while temp:
            cache[counter] = temp
            temp = temp.next
            counter += 1
        index = counter - 1
        value = head
        while index > counter // 2:
            temp = value.next
            value.next = cache[index]
            value.next.next = temp
            value = temp
            index -= 1
        if counter % 2 == 0:
            value.next.next = None
        else:
            value.next = None

        result = []
        while head:
            result.append(head.val)
            head = head.next
        print(result)

        
        
if __name__ == "__main__":
    node = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, ListNode(6))))))
    Solution().reorderList(node)