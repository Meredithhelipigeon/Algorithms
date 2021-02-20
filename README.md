# Algorithms

## Arithemetic Slices: 
Arithmetic Slices function should return the number of arithmetic slices in the array A.  
Algorithm:  
Step 1. Utilize a vector to store the difference between two nearby items.  
Step 2. If two numbers are the same, it means that it will increase 1+overlap(the accumulation for last item) slices.  
Edge Cases: 
- The number of sequence is less than 3;
- [1,2,3,-1,-5]
