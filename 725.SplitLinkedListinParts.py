from typing import Optional, List

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        cache = []
        count = 0
        current = head
        while current:
            tmp = current
            current = current.next
            tmp.next = None
            cache.append(tmp)
            count += 1
        
        min_node_len = count // k
        max_node_len = min_node_len + 1

        node_with_max_len = count % k
        result = []


        for _ in range(node_with_max_len):
            node_to_insert: ListNode = ListNode()
            tmp = node_to_insert
            for _ in range(max_node_len):
                node = cache.pop(0)
                tmp.next = node
                tmp = tmp.next
            result.append(node_to_insert.next)

        for _ in range(k-node_with_max_len):
            node_to_insert: ListNode = ListNode()
            tmp = node_to_insert
            for _ in range(min_node_len):
                node = cache.pop(0)
                tmp.next = node
                tmp = tmp.next
            result.append(node_to_insert.next)
        
        return result




if __name__ == "__main__":
    nodes = Solution().splitListToParts(
        ListNode(val=1, next=ListNode(val=2, next=ListNode(val=3))),
        k=5
    )
    for item in nodes:
        result = []
        while item:
            result.append(item.val)
            item = item.next
        print(result)
