from typing import Optional


class Solution:
        def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
            sum1=''
            sum2=''
            for i in l1:
                sum1+=i 
            for i in l2:
                sum2+=i
            sumall = int(sum1)+int(sum2)
            for i in sumall:
                Optional.append(i)
            result.reverse() 
            return result
