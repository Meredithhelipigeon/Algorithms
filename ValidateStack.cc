class Solution {

public:
    int find_int(vector<int>& v, int p){
        for(auto i = 0; i < v.size();++i){
            if(p==v[i]) return i;
        }
        return -1;
    }
    
    
    bool validateStackSequences(vector<int>& pushed, vector<int>& popped) {
        if(pushed.size()==0) return true;
        int maxInd = 0;
        vector<int> Order;
        vector<int> s;
        for(auto p: popped){
            std::vector<int>::iterator judge = find (Order.begin(), Order.end(), p);
            bool x = judge!=Order.end();
            cout << p << " "<< x << endl;
            if((judge!=Order.end())&&(p==Order.back())){
                Order.erase(Order.end()-1);
                s.push_back(p);
            } else if((judge!=Order.end())&&(p!=Order.back())){
                cout << judge-Order.begin() << endl;
                cout << p << endl;
                return false;
            } else {
                Order.clear();
                maxInd=find_int(pushed, p);
                if(maxInd==-1) return false;
                for(int i=0;i<maxInd;++i){
                    auto j = find(s.begin(),s.end(),pushed[i]);
                    if(j==s.end()){
                        Order.push_back(pushed[i]);
                    }
                }
                cout << maxInd << endl;
                for(auto v :Order) cout << v << " ";
                cout << endl;
                s.push_back(p);
            }
        }
        return true;
    }
};
