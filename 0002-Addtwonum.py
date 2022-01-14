class Solution(object):
    def addTwoNumbers(self, l1, l2):
        i = 0
        a = 0
        b = 0
        while l1:
            a = a+l1.val*(10**i)
            l1 = l1.next
            i = i+1
        i = 0
        while l2:
            b = b+l2.val*(10**i)
            l2 = l2.next
            i = i+1
        c = a+b
        d = [int(i) for i in str(c)]
        d.reverse()
        

        head = ListNode(d[0])
        current = head
        for i in d[1:]:
            current.next = ListNode(i)
            current = current.next

        return head
