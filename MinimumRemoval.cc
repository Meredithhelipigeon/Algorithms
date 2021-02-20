// Minimum Remove to Make Valid Parentheses. Your task is to remove 
//  the minimum number of parentheses ( '(' or ')', in any positions ) 
//  so that the resulting parentheses string is valid and return any 
//  valid string.

class Solution {
public:
    string minRemoveToMakeValid(string s) {
        vector<int> PosLen;
        for(int i = 0; i < s.size();){
            if (s[i]==')'){
                if (!PosLen.empty()){
                    PosLen.pop_back();
                    ++i;
                } else {
                    s.erase(s.begin()+i);
                }
            } else if (s[i]=='(') {
                PosLen.push_back(i);
                ++i;
            } else {
                ++i;
            }
        }
        if(PosLen.size()>=0){
            for(int i = 0; i < PosLen.size();++i){
                s.erase(s.begin()+PosLen[i]-i);
            }
        }
        // cout << PosLen.size() << endl;
        // cout << PosLen[0] << endl;
        return s;
    }
};


