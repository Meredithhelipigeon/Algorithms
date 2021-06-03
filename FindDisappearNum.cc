class Solution {
public:
    vector<int> findDisappearedNumbers(vector<int>& nums) {
        vector<int> MyHashMap(nums.size());
        for(auto elem:nums){
            MyHashMap[elem-1]=1;
        }
        vector<int> ans;
        int index=0;
        for(auto elem: MyHashMap){
            if (elem==0){
                ans.push_back(index+1);
            }
            index+=1;
        }
        return ans;
    }
};
