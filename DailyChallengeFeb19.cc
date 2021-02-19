// Arithmetic Slices The function should return the number of arithmetic slices in the array A.

class Solution {
public:
    int numberOfArithmeticSlices(vector<int>& A) {
        int overlap = 0;
        int num = 0;
        if(A.size()>2){
            // use a vector to store the difference of the neighbor items
            vector<int> diff;
            for(int i = 0; i < A.size()-1; i++){
                diff.push_back(A[i+1]-A[i]);
            }
            // if two numbers are the same, it means that there are at least one
            //  arithmetic arrays and the number of extra arrays depends on the overlapping
            //  array from the last item
            for(int i = 0; i < A.size()-2; i++){
                if(diff[i]==diff[i+1]){
                    num += 1+overlap;
                    overlap+=1;
                } else {
                    overlap = 0;
                }
            }
        }
        return num;
    }
};
