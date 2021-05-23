class Solution {
public:

multimap<int, int> flip_map(map<int,int> & src) {

    multimap<int,int> dst;

    for(typename map<int, int>::const_iterator it = src.begin(); it != src.end(); ++it)
        dst.insert(pair<int, int>(it -> second, it -> first));

    return dst;
}
    vector<int> topKFrequent(vector<int>& nums, int k) {
        std::map<int,int> mymap;
        for(auto n: nums){
            if (mymap.find(n) != mymap.end()){
                mymap[n]-=1;
            } else {
                mymap[n]=-1;
            }
        }
        std::multimap<int, int> dst = flip_map(mymap);
        int i = 0;
        vector<int> ans;
        for(auto p: dst){
            if (i<k) {
                ans.push_back(p.second);
            } else {
                break;
            }
            i+=1;
        }
        return ans;
    }
};
