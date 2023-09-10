class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


class Solution:
    def hascycle(self, head):
        slow = head
        fast = head
        while fast != None and fast.next != None:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return 1
            return 0


obj = Solution()
head = Node(1)
head.next = Node(3)
head.next.next = Node(3)
head.next.next.next = Node(4)
print(obj.hascycle(head))
