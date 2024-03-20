from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeZeroSumSublists(self, head: Optional[ListNode]) -> Optional[ListNode]:

        order: list = []
        target = head


        while target:
            if target.val != 0:
                order.append(target.val)
            target = target.next
        
        result = self.remove_zero_sequences(order)

        value = ListNode()
        node = value
        for num in result:
            node.next = ListNode(num)
            node = node.next
        return value.next
        

    def remove_zero_sequences(self, nums: list):
        start = 0
        while start < len(nums):
            end = start
            total = 0
            while end < len(nums) and total + nums[end] != 0:
                total += nums[end]
                end += 1
            if end < len(nums):
                if total + nums[end] == 0:
                    del nums[start:end+1]
            else:
                start += 1
        return nums
        

                

    


        

if __name__ == "__main__":
    listnode = ListNode(1, ListNode(2, ListNode(-3, ListNode(3, ListNode(1)))))
    Solution().removeZeroSumSublists(listnode)