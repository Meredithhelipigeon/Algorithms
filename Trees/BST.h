#ifndef BST_H
#define BST_H
#include <iostream>
using namespace std;

class TreeNode {
public:
	TreeNode * pLeft;
	TreeNode * pRight;
	TreeNode * pParent;
	int key;
	int field;

	TreeNode();
	~TreeNode();
	void print();
	void print(int indent);
	void preOrder();
	void inOrder();
};

class BST {
public:
	TreeNode * pRoot;

	BST();
	~BST();

        TreeNode * insert(int k);
        TreeNode * search(int k);

	// print functions 
	void preOrder();
	void inOrder();
	void print();
};
#endif
