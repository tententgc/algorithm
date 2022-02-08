# Given a linked list, remove the nth node from the end of the list and return its head.
# 
# Follow up: Could you do this in one pass?
# 
# # Solution
# # 
# # | **Time** | **Space** |
# # |---|---|
# # | O(n) | O(1) |
# # 
# #
class Solution:
    def removeNthFromEnd(self, head, n):
        def index(node):
            if not node:
                return 0
            i = index(node.next) + 1
            if i > n:
                node.next.val = node.val
            return i
        index(head)
        return head.next
