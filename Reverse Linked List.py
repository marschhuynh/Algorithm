# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

head = None
last = None

for i in range(4):
    node = ListNode(i)
    if last is None:
        last = node
        head = last
    else:
        last.next = node
        last = node


class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head:
            if head.next:
                current = head.next
                last = head
                last.next = None
                while current.next:
                    next = current.next
                    current.next = last
                    last = current
                    current = next
                current.next = last
                return current
            else:
                return head
        return head

current = Solution().reverseList(head)
# current = head

while (current):
    print(current.val)
    current = current.next
