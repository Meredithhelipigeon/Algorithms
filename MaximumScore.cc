class Solution {
public:
    int maximumScore(vector<int>& nums, int k) {
        int maximum = nums[k];
        int currentMin = nums[k];
        int left = k;
        int right = k;
        while((left>0)||(right< nums.size()-1)){
            if((left==0)||(nums[left-1]<nums[right+1])){
                if(nums[right+1]<currentMin) currentMin = nums[right+1];
                right+=1;
            } else {
                if(nums[left-1]<currentMin) currentMin = nums[left-1];
                left-=1;
            }
            int current=currentMin*(right-left+1);
            if(current>maximum) maximum = current;
        }
        return maximum;
    }
};
