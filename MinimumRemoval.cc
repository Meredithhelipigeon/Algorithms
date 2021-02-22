// Minimum Remove to Make Valid Parentheses. Your task is to remove 
//  the minimum number of parentheses ( '(' or ')', in any positions ) 
//  so that the resulting parentheses string is valid and return any 
//  valid string.

class Solution {
public:
    string minRemoveToMakeValidV1(string s) {
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

    string minRemoveToMakeValidV2(string s) {
        stack<int> PosLen;
        for(int i = 0; i < s.size();++i){
            if (s[i]==')'){
                if (!PosLen.empty()){
                    PosLen.pop();
                } else {
                    s[i]='N';
                }
            } else if (s[i]=='(') {
                PosLen.push(i);
            }
        }
        
        // Replace the removal characters to 'N'
        if(PosLen.size()>=0){
            int num = PosLen.size();
            for(int i = 0; i < num;++i){
                int j = PosLen.top();
                PosLen.pop();
                s[j]='N';
            }
        }
        
        
        string ans ="";
        for(int i = 0; i<s.size();++i){
            if(s[i]!='N'){
             ans += s[i];   
            }
        }
        return ans;
    }
};


