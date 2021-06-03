class Solution {
public:
    void moveZeroes(vector<int>& nums) {
        int num = nums.size();
        int cur = 0;
        for(int i=0;i<num;++i){
            if (nums[cur]==0){
                nums.erase(nums.begin()+cur);
                nums.push_back(0);
            } else {
                cur+=1;
            }
        }
    }
};
