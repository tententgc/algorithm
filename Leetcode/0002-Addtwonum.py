class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        num1 = num2 = counter = 0

        while l1:
            num1 += l1.val * 10 ** counter
            l1 = l1.next
            counter += 1
        counter = 0

        while l2:
            num2 += l2.val * 10 ** counter
            l2 = l2.next
            counter += 1

        sumres = num1 + num2
        res = str(sumres)
        answer = [x for x in res]
        answer.reverse()

        head = ListNode()
        ans = head
        for digit in answer:
            ans.next = ListNode(digit)
            ans = ans.next

        return head.next
