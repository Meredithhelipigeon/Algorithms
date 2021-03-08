class Solution {
public:
    int removePalindromeSub(string s) {
        if(s.size()==0) return 0;
        string rev = s;
        reverse(s.begin(),s.end());
        if(rev==s) return 1;
        else return 2;
    }
};
