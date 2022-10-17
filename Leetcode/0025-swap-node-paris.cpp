class Solution
{
public:
    ListNode *swapPairs(ListNode *head)
    {

        if (!head || !head->next)
            return head;

        ListNode *tmp = new ListNode(0);
        tmp->next = head;

        ListNode *curr = tmp;

        while (curr->next && curr->next->next)
        {
            ListNode *n1 = curr->next;
            ListNode *n2 = curr->next->next;

            n1->next = n2->next;
            curr->next = n2;
            curr->next->next = n1;
            curr = curr->next->next;
        }

        return tmp->next;
    }
};