class Solution {
public:
    void sortColors(vector<int>& nums) {
        int RedNum = 0;
        int WhiteNum = 0;
        int BlueNum = 0;
        for (auto color: nums){
            if (color==0){
                RedNum+=1;
            } else if(color==1){
                WhiteNum+=1;
            } else {
                BlueNum+=1;
            }
        }
        // Add Red
        for(int i = 0;i<RedNum;++i){
            nums[i]=0;
        }
        for(int i = RedNum;i<WhiteNum+RedNum;++i){
            nums[i]=1;
        }
        for(int i = RedNum+WhiteNum;i<BlueNum+WhiteNum+RedNum;++i){
            nums[i]=2;
        }
    }
};
