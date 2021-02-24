class Solution {
public:
    int check_if_exists(string s, string k){
        int pos = 0;
        for(int i = 0; i < k.size(); ++i){
            pos = s.find_first_of(k[i]);
            if(pos==-1) return -1;
            s.erase(s.begin(), s.begin()+pos+1);
        }
        return k.size();
    }
    
    
    string findLongestWord(string s, vector<string>& d) {
        string ans = "";
        int max_num = 0;
        for(auto k: d){
            int dir = check_if_exists(s,k);
            if((dir>max_num)||((dir==max_num)&&(ans>k))){
                ans=k;
                max_num=dir;
            } 
        }
        return ans;
    }
};
