# Merge two sorted linked lists and return it as a new list.
# 
# Here's a one line summary of the above code: Merge two sorted linked lists and return it as a new
# list.
# 
# Here's a short code snippet:
# 
# def mergeTwoLists(self, a, b):
#     if a and b:
#         if a.val > b.val:
#             a, b = b, a
#         a.next = self.mergeTwoLists(a.next, b)
#     return a or b
class Solution:
    def mergeTwoLists(self, a, b):
        if a and b:
            if a.val > b.val:
                a, b = b, a
            a.next = self.mergeTwoLists(a.next, b)
        return a or b
