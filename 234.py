class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def isPalindrome(self, head) -> bool:
        if not head:
            return False
        pre = self.findmidpre(head)
        print("pre is ",pre.val)
        prenext = pre.next
        print("pre next is ",prenext.val)
        prenext = self.reverse(prenext)
        print("pre next after reverse is ",prenext.val)
        p , q = head, prenext
        print(p,q)
        while p and q:
            print("p.val is ",p.val,'q.val is ',q.val)
            if p.val != q.val:
                return False
        return True
    
    def findmidpre(self,head):
        q = ListNode()
        q.next = head
        if not head:
            return head
        slow , fast = head, head
        while fast and fast.next:
            pre = slow
            slow = slow.next
            fast = fast.next
            fast = fast.next
        return pre
    def reverse(self,head):
        if not head:
            return head
        prev = None
        curr = head
        while curr:
            pend = curr.next
            curr.next = prev
            prev = curr
            curr = pend
            
        return prev

if __name__ == '__main__':
    head = ListNode()
    k = head
    for i in range(2):
        p = ListNode(i)
        head.next = p
        head = head.next
    p = head = k.next
    while p:
        print("p . val is ",p.val)
        p = p.next
    solu = Solution()
    s = solu.isPalindrome(head)
    print(s)