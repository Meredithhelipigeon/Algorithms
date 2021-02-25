class Solution {
public:
    int two_ex(int e){
        int num = 1;
        for(int i = 0;i<e;++i){
            num *=2;
        }
        return num;
    }
    
    int scoreOfParentheses(string S) {
        int num = 0;
        int ans = 0;
        for(int i = 0; i < S.length(); ++i){
            if(S[i]=='('){
                num += 1;
            } else if(S[i-1]=='('){
                num -= 1;
                ans += two_ex(num);
            } else {
                num -= 1;
            }
        }
        return ans;
    }
};

