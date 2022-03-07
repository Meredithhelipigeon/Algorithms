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
    ListNode* mergeTwoLists(ListNode* list1, ListNode* list2) {
        ListNode *cur = new ListNode(-1);
        ListNode *dummy = cur;
        while ((list1!=NULL) || (list2!=NULL) ){
            if ((list1!=NULL) && (list2!=NULL)) {
                int el1=list1->val;
                int el2=list2->val;
                if (el1<el2){
                    cur->next= list1;
                    list1=list1->next;
                } else {
                    cur->next = list2;
                    list2=list2->next;
                }
            } else if (list1!=NULL){
                cur->next= list1;
                list1=list1->next;
            } else {
                cur->next= list2;
                list2=list2->next;
            }
            cur=cur->next;
        }
        return dummy->next;
    }
};

