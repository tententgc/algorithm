class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        prev = None
        curr_val = head.val
        prev = curr
        curr = curr.next

        while curr:
            if curr.val == curr_val:
                prev.next = curr.next
            else:
                curr_val = curr.val
                prev = curr
            curr = curr.next
        return head
