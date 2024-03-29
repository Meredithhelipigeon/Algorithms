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

## Encode and Decode TinyURL[System Design]:  
Description: Design the encode and decode methods for the TinyURL service. There is no restriction on how your encode/decode algorithm should work. You just need to ensure that a URL can be encoded to a tiny URL and the tiny URL can be decoded to the original URL.  
Algorithm: 
We map the last 6 characters of the original URL to characters from [A-Z],[a-z],[0,9] with hash function ord(n)%62 to generate the short URL. And then we store [shortURL, longURL] in a dictionary. We return the long URL by the dictionary.  

## Maximize Number of Nice Divisors
Description: You are given a positive integer primeFactors. You are asked to construct a positive integer n that satisfies the following conditions:  
1) The number of prime factors of n (not necessarily distinct) is at most primeFactors.
2) The number of nice divisors of n is maximized. Note that a divisor of n is nice if it is divisible by every prime factor of n. For example, if n = 12, then its prime factors are [2,2,3], then 6 and 12 are nice divisors, while 3 and 4 are not.

Return the number of nice divisors of n. Since that number can be too large, return it modulo 10^9 + 7.
Algorithm: We realize that divide them into 3 and 2 is the most efficient. Therefore, we try to split it in 3 and 2. 
Version 2: How to approach the number of 3: O(logn), keep track of where to square and where to plus one(use a stack to denote)  
Version 3: Use the library "pow(base, times, modNumber)" built in Python. The time efficiency is also O(log n)  
Time effciency: O(log n)

## Evaluate the Bracket Pairs of a String
Description: You are given a string s that contains some bracket pairs, with each pair containing a non-empty key.  
Time Efficency: O(len(knowledge)+len(string))  
Algorithm: First change the Lists into the dictionary because in python, dictionary works the same as hash table. So the time efficiency is increased largely by using dictionary for serach. And then we walk through the string and replace the key with the value or question mark by searching in the dictionary.  

## Minimum Number of Operations to Reinitialize a Permutation
Algorithm: This is intuitive  
Concept in Python: if we want deep copy, we should import copy library and use "copy.copy(list1)". If we purely use operator "assignment", the new list and the old list will change sumultaneously.

## Number of Different Integers in a String  
Descrption: You are given a string word that consists of digits and lowercase English letters.  You will replace every non-digit character with a space. For example, "a123bc34d8ef34" will become " 123  34 8  34". Notice that you are left with some integers that are separated by at least one space: "123", "34", "8", and "34".  Return the number of different integers after performing the replacement operations on word.  
Strategy: deal with leading zero: if the last stored string is "0" we then update with the new character(it could prevent us from deleting the "0").  

## Keys and Rooms
Description:  
There are N rooms and you start in room 0.  Each room has a distinct number in 0, 1, 2, ..., N-1, and each room may have some keys to access the next room. 

Formally, each room i has a list of keys rooms[i], and each key rooms[i][j] is an integer in [0, 1, ..., N-1] where N = rooms.length.  A key rooms[i][j] = v opens the room with number v.

Initially, all the rooms start locked (except for room 0). 

You can walk back and forth between rooms freely.

Algorithm: Have a list of frontier and use this frontier to open new rooms. We then update the frontier. "dynamical change". Mark the visited room to prevent "revisit".  
Optimization: When visiting the room, calculate the number instead of calculating the number after updating the checklist for all rooms, which takes O(n).  

## Pacific Atlantic Water Flow
Description:   
You are given an m x n integer matrix heights representing the height of each unit cell in a continent. The Pacific ocean touches the continent's left and top edges, and the Atlantic ocean touches the continent's right and bottom edges.

Water can only flow in four directions: up, down, left, and right. Water flows from a cell to an adjacent one with an equal or lower height.

Return a list of grid coordinates where water can flow to both the Pacific and Atlantic oceans.  
Algorithm: BFS. Have a list of frontier and use this frontier to add new states.  
Strategy: directin array direction = [[0,1],[0,-1],[1,0],[-1,0]]

## Flip Binary Tree To Match Preorder Traversal
Description: You are given the root of a binary tree with n nodes, where each node is uniquely assigned a value from 1 to n. You are also given a sequence of n values voyage, which is the desired pre-order traversal of the binary tree.

Flip the smallest number of nodes so that the pre-order traversal of the tree matches voyage.

Return a list of the values of all flipped nodes. 

Algorithm: use DFS to search.   
Strategy: collections.deque()  
Optimization: Do not change the original list voyage to increase the time efficiency.

## Russian Doll Envelopes
Description: You are given a 2D array of integers envelopes where envelopes[i] = [wi, hi] represents the width and the height of an envelope.

One envelope can fit into another if and only if both the width and height of one envelope are greater than the other envelope's width and height.

Return the maximum number of envelopes you can Russian doll (i.e., put one inside the other).

Algorithm: First sort the envelopes by width. And the problem then becomes finding the longest increasing numbers in this array.  
Time Efficiency: O(nlogn)

## Palindrome Linked List
Description: Given the head of a singly linked list, return true if it is a palindrome.  

Algorithm: Use fast and slow algorithm to get the median of a linked list. Reverse the part before the median. Check the list of the first part and the second part.

Time Efficiency: O(n) time and O(1) space

## Ones and Zeroes
Description: You are given an array of binary strings strs and two integers m and n.

Return the size of the largest subset of strs such that there are at most m 0's and n 1's in the subset.

A set x is a subset of a set y if all elements of x are also elements of y.

Algorithm: Form a DP matrix((n+1)*(m+1)). Add element from the string list one by one. Update the DP matrix from n->0, m->0.

Time efficiency: O(len(str)\*m\*n)

## Longest Increasing Path in a Matrix:
Descrption:  
Given an m x n integers matrix, return the length of the longest increasing path in matrix.

From each cell, you can either move in four directions: left, right, up, or down. You may not move diagonally or move outside the boundary (i.e., wrap-around is not allowed).

Algorithm:  
Use DFS to search the depth of each path based on the starting point. While calculating the depth of each point, we may use the previous calculation. Hence, import python functools-Iru_cache().

Time Efficiency: O(n^2)

## Deepest Leaves Sum
Description: Given the root of a binary tree, return the sum of values of its deepest leaves.

Algorithm: Since we calculate the leaves in the deepest layer, it is easy to think of BFS. We use BFS and sum up the leaves in the deepest layer. 

Time Efficiency: O(n)

## Beautiful Arrangement(2)
Description:  
Given two integers n and k, you need to construct a list which contains n different positive integers ranging from 1 to n and obeys the following requirement:
Suppose this list is [a1, a2, a3, ... , an], then the list [|a1 - a2|, |a2 - a3|, |a3 - a4|, ... , |an-1 - an|] has exactly k distinct integers.

If there are multiple answers, print any of them.

Algorithm:  
If we want every difference distinct, we use the smallest, the biggest respectively... So if we want k distinct difference, we use that strategy to find k-1 distinct elements and then the others are placed within the difference of 1.

Time Efficiency: O(n)

## Flatten Nested List Iterator:
Description:
You are given a nested list of integers nestedList. Each element is either an integer or a list whose elements may also be integers or other lists. Implement an iterator to flatten it.

Algorithm:
Use the recursion to break the list.  
While iterating the list, don't change the data structure.

## Maximum Size Subarray Sum Equals k:  
Description: 
Given an integer array nums and an integer k, return the maximum length of a subarray that sums to k. If there isn't one, return 0 instead.  

Algorithm:  
Step 1. calculate the prefix array `sub`.  
Step 2. (if sub[i]-sub[j]==k => it means that there is an subarray sums to k.). 
        use a hashmap to locate 'sub'.
Step 3. find out the "difference" by hashmap.  

## Jump Game:  
Description:  
You are given an integer array nums. You are initially positioned at the array's first index, and each element in the array represents your maximum jump length at that position.  

Return true if you can reach the last index, or false otherwise.  

Algorithm:  
Solution 1. Define a DP and let DP[i] as the boolean denoting whether we could go to the last index(recurrence is super easy).  
Time complexity is O(mn).  
Solution 2. Since at each step, nums[i] denotes the max gap that we could jump(continuously), nums[i]+i is the maximum length that we could jump. Keeping track of the max length could solve the problem.
Time complexity is O(n).  

## Stock Price Flucuation:  
Description:  
You are given a stream of records about a particular stock. Each record contains a timestamp and the corresponding price of the stock at that timestamp.  

Unfortunately due to the volatile nature of the stock market, the records do not come in order. Even worse, some records may be incorrect. Another record with the same timestamp may appear later in the stream correcting the price of the previous wrong record. 

Design an algorithm that:

Updates the price of the stock at a particular timestamp, correcting the price from any previous records at the timestamp.  
Finds the latest price of the stock based on the current records. The latest price is the price at the latest timestamp recorded.  
Finds the maximum price the stock has been based on the current records.  
Finds the minimum price the stock has been based on the current records.  

Algorithm:  
1. Use a maxHeap and a minHeap to store the price and timestamp.  
2. Use a dictionary to store the current price and timestamp pair.  
3. Get maximum: pop the maxHeap until there is a current version pair.

Time Complexity:  
1. 'update': O(logn).  
2. 'max'/'min': O(nlogn).  
3. 'current': O(1).  

How to think of this algorithm:  
dynamic min => minHeap => Add a rule, pop following the rule (accepted)  
dynamic min => minHeap => Update immediately => low efficiency (unaccepted)

## Word Search:  
Description:  
Given an m x n grid of characters board and a string word, return true if word exists in the grid.

The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once.  

Algorithm:  
Using backtrack to make sure that for each path, we mark visited and revert back if there is no solution.
