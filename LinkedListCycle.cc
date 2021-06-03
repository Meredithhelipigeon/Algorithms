/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    bool hasCycle(ListNode *head) {
        if ((head==NULL)||(head->next==NULL)||(head->next==NULL)){
            return false;
        }
        ListNode* cur1=head->next;
        ListNode* cur2=head->next->next;
        while(!((cur1==cur2)||(cur1==NULL)||(cur2==NULL))){
            cur1=cur1->next;
            if (cur2->next==NULL){
                cur2=NULL;
            } else {
                cur2=cur2->next->next;
            }
        }
        if ((cur1==NULL)||(cur2==NULL)) {
            return false;
        } else {
            return true;
        }
    }
};
