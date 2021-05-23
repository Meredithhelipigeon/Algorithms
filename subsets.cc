class Solution {
public:
    vector<vector<int>> subsets(vector<int>& nums) {
        vector<vector<int>> binaryNum;
        int length = nums.size();
        int comninatoricsNum = pow(2,length);
        for(int i = 0;i<comninatoricsNum;++i){
            vector<int> current;
            int j = i;
            if (j==0){
                current.push_back(0);
            }
            while (j>0) {
                if (j%2==0){
                    current.push_back(0);
                } else {
                    current.push_back(1);
                }
                j/=2;
            }
            binaryNum.push_back(current);
        }
        
        vector<vector<int>> ans;
        for(auto x: binaryNum){
            int i = 0;
            vector<int> current;
            for(auto index: x){
                if (index==1){
                    current.push_back(nums[length-i-1]);
                }
                i+=1;
            }
            ans.push_back(current);
        }
        return ans;
    }
};
