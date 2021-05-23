/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* mergeTwoLists(ListNode* l1, ListNode* l2) {
        ListNode* past= new ListNode();
        ListNode* current=past;
        while((l1!=NULL)||(l2!=NULL)){
            if ((l1!=NULL)&&(l2!=NULL)) {
                if (l1->val>=l2->val) {
                    current->next = l2;
                    l2=l2->next;
                } else{
                    current->next=l1;
                    l1=l1->next;
                }
                current = current->next;
            } else if (l1!=NULL) {
                current->next = l1;
                current = l1;
                l1=l1->next;
            } else if (l2!=NULL) {
                current->next = l2;
                current = l2;
                l2=l2->next;
            }
        }
        return past->next;
    }
};
