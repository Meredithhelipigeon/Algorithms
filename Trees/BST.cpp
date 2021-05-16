#include "BST.h"
#include <iostream>
#include <fstream>
#include <random>
#include <math.h>

TreeNode::TreeNode() {
	pLeft = NULL; pRight = NULL; pParent = NULL; key = 0; field = 0;
}

TreeNode::~TreeNode() {
	if (pLeft != NULL) { delete pLeft; pLeft=NULL; }
	if (pRight != NULL) { delete pRight; pRight=NULL; }
}

void TreeNode::print() {
	this->print(0);
}

void TreeNode::print(int indent) {	
// this function is purely for your own testing purposes; we will
// not be calling it.  In particular, this is one place where you can
// change what's being done (e.g. you might want to print the field)
	int offset = 3;

	if (pRight != NULL) {
		pRight->print(indent + offset);
	}
	if (pParent != NULL) { // lets print a link to the parent so we can see better
		for (int i = 0; i < indent-offset; i++) cout << " ";
		if (this == pParent->pRight) cout << "/"; else cout << "\\";
		for (int i = 0; i < offset - 1; i++) cout << "-";
	} 
	else { // no parent-references?  Well, at least print indented
		for (int i = 0; i < indent; i++) cout << " ";
	}
	cout << this->key << " " << this->field << "\n"; 
	if (pLeft != NULL) {
		pLeft->print(indent + offset);
	}
}

void TreeNode::preOrder() {
	cout << " " << this->key;
	if (this->pLeft != NULL) this->pLeft->preOrder();
	if (this->pRight != NULL) this->pRight->preOrder();
}

void TreeNode::inOrder() {
	if (this->pLeft != NULL) this->pLeft->inOrder();
	cout << " " << this->key;
	if (this->pRight != NULL) this->pRight->inOrder();
}
 
BST::BST() {
	pRoot = NULL;
}

BST::~BST() {
	if (pRoot != NULL) {delete pRoot; pRoot=NULL;}
}

TreeNode * BST::insert(int k) {
// pre: k is not in the tree
// post: returns node where k was added
	TreeNode * pNewNode = new TreeNode();
	pNewNode->key = k;

	if (pRoot == NULL) {
		pRoot = pNewNode;
	}
	else {
		TreeNode * pParent = pRoot;
		TreeNode * pChild = pRoot;
	
		do {
			pParent = pChild;
			if (k<pParent->key) {	
				pChild = pParent->pLeft;
			}
			else {
				pChild = pParent->pRight;
			}
		}
		while (pChild != NULL);

		// pChild is now empty subtree, need to figure out where to put new one
		if (k < pParent->key) {
			pParent->pLeft = pNewNode;
		} 
		else {
			pParent->pRight = pNewNode;
		}
		pNewNode->pParent = pParent;
	}

	return (pNewNode);
}	

TreeNode * BST::search(int k) {
// post: returns node where k is, or NULL
	TreeNode * pParent = pRoot;
	TreeNode * pChild = pRoot; 

	do {
		pParent = pChild;

		if (k < pParent->key) {	
			pChild = pParent->pLeft;
		}
		else {
			if (k > pParent->key) {	
				pChild = pParent->pRight;
			}
			else { // found the key k
				return pParent;
			}
		}
	}
	while (pChild != NULL);

	return NULL;
}


void BST::print() {
	this->pRoot->print();
}

void BST::preOrder() {
	this->pRoot->preOrder();
	cout << "\n";
}
void BST::inOrder() {
	this->pRoot->inOrder();
	cout << "\n";
}

