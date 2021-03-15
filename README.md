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

## Add One Row to Tree: 
Description: Given the root of a binary tree, then value v and depth d, you need to add a row of nodes with value v at the given depth d. The root node is at depth 1.  
Time Efficiency: O(log)  
Algorithm:  
Find every tree at depth N-1 and change its left subtree and right subtree to the new trees. Also let the left subtree and right subtree be under the new trees.  
(Use DFS recursion) 

## Group the People Given the Group Size They Belong To:  
Description: There are n people that are split into some unknown number of groups. Each person is labeled with a unique ID from 0 to n - 1.You are given an integer array groupSizes, where groupSizes[i] is the size of the group that person i is in. For example, if groupSizes[1] = 3, then person 1 must be in a group of size 3. Return a list of groups such that each person i is in a group of size groupSizes[i].  
Time Efficiency: O(n)  
Algorithm:  
Classify the elements in the group size through direct hashing. Then if the number is full, generalize a group.  

## Maximum Score of a Good Subarray[Greedy Algorithm]:
Description: You are given an array of integers nums (0-indexed) and an integer k. The score of a subarray (i, j) is defined as min(nums[i], nums[i+1], ..., nums[j]) * (j - i + 1). A good subarray is a subarray where i <= k <= j. Return the maximum possible score of a good subarray.  
Time Efficiency: O(n)  
Algorithm:
We want to find the best combinations near the index k. There are (k-1)\*(n-k) different combinations, which is in O(n^2) if we want to calculate each of them. It is too much so that we consider at one step, we tend to choose the larger one since the coverage is the same. And we consider that to decide go left and right until the whole array is visited.  

