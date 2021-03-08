# Algorithms
This repository keeps records of generated algorithms and edge cases towards different types of coding problems.

## Arithemetic Slices: 
Description: Arithmetic Slices function should return the number of arithmetic slices in the array A.  
Time Efficiency: O(n).  
Algorithm:  
Step 1. Utilize a vector to store the difference between two nearby items.  
Step 2. If two numbers are the same, it means that it will increase 1+overlap(the accumulation for last item) slices.  
Edge Cases: 
- The number of sequence is less than 3;
- [1,2,3,-1,-5]

## Remove Palindromic Subsequences:   
Description: Given a string s consisting only of letters 'a' and 'b'. In a single step you can remove one palindromic subsequence from s. Return the minimum number of steps to make the given string empty.  
Time Efficiency: O(n).  
Algorithm:  
The number is at most 2 because if we first subtract all the 'a' and then subtract all the 'b', it is done.  
If it is a palindromic sequence, return 1.  
If it is empty, return 0.  
Libraries:  
C++: std::reverse(a.begin(),a.end()) -> will change a string.  
