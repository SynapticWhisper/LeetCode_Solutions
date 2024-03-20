class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Solution №1
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:

        new = self.get_node_end(list2)
        past = self.get_node_past(list1, b)
        new.next = past
        
        node = list1
        counter = 0
        while node:
            if counter != a - 1:
                node = node.next
                counter += 1
            else:
                node.next =  list2
                break
        return list1
        

    def get_node_end(self, node: ListNode) -> ListNode:
        result = node
        while result.next:
            result = result.next
        return result

    def get_node_past(self, node: ListNode, index: int) -> ListNode:
        counter = 0
        result = node
        while counter <= index and node:
            result = result.next
            counter += 1
        return result
    
# Solution №2
class Solution_2:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        result = ListNode()
        r_help = result
        counter = 0
        node = list1
        while node:
            if counter < a:
                r_help.next = node
                node = node.next
                counter += 1
            elif counter == a:
                r_help.next = list2
                r_help = self.get_node_end(list2)
                node = node.next
                counter += 1
            elif a < counter <= b:
                node = node.next
                counter += 1
            else:
                r_help.next = node
                break
        return result
    
    def get_node_end(self, node: ListNode) -> ListNode:
        result = node
        while result.next:
            result = result.next
        return result
    
if __name__ == "__main__":
    node_1 = ListNode(0, ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, ListNode(6)))))))
    node_2 = ListNode(1000000, ListNode(1000001, ListNode(1000002, ListNode(1000003, ListNode(1000004)))))
    Solution_2().mergeInBetween(node_1, 2, 5, node_2)