class ListNode:
    def __init__(self,val):
        self.val = val
        self.next = None

class Solution:
    from typing import Optional
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        def findmid(head):
            if not head:
                return head
            slow , fast = head , head
            while fast and fast.next:
                slow = slow.next
                fast = fast.next
                fast = fast.next
            return slow
        return findmid(head)
    def reverse(self,head):
        prev = None
        curr = head
        while curr:
            pend = curr.next
            curr.next = prev
            prev = curr
            curr = pend
        return prev
if __name__ == '__main__':
    Solu = Solution()
    head = ListNode(-1)
    p = head# .next
    for i in range(5):
        q = ListNode(i)
        p.next = q
        p = p.next
    pend = head.next
    head.next = None

    pend = Solu.reverse(pend)
    while pend:
        print("pend value is ",pend.val)
        pend = pend.next
    