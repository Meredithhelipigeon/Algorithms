/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution1 {
public:
    bool hasCycle(ListNode *head) {
        ListNode *step1 = head;
        ListNode *step2 = head;
        bool first = true;
        while (step1 && step2){
            if (first) {
                first=false;
            } else {
                if (step1 == step2){
                    return true;
                }
            }
            step1=step1->next;
            step2=step2->next;
            if (step2) {
                step2=step2->next;
            }
        }
        return false;
    }
};

class Solution2 {
public:
    bool hasCycle(ListNode *head) {
        if (head==NULL) {
            return false;
        }
        // set the start point differently
        ListNode *step1 = head;
        ListNode *step2 = head->next;
        while (step1 != step2){
            if (!step2 || !(step2->next)){
                return false;
            }
            step1=step1->next;
            step2=step2->next->next;
        }
        return true;
    }
};

