class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Solution:
    def reverse(self, head):
        if head is None or head.next is None:
            return head
        prev = None
        curr = head
        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        return prev

    def printList(self, head):
        while head:
            print(head.data, end=" ")
            head = head.next
        print()


obj = Solution()
head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)
obj.printList(head)
head = obj.reverse(head)
obj.printList(head)


"""
Recursive

def reverseList(head, prev=None):
    if not head:
        return prev
    next = head.next
    head.next = prev
    return self.reverseList(next, head)
    
"""
