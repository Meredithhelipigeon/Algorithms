#include <iostream>
#include <algorithm>
#include <fstream>
#include <random>
#include <math.h>
#include "BST.h"
#include <stack>
#include <vector>

using namespace std;
int rotNum = 0;

// Helper function for AVLTree
int height(TreeNode * z){
	return z->field;
}

void change_height(TreeNode * z, int height){
	z->field = height;
}

void setHeightFromSubtrees(TreeNode * z){
	int left = -1;
	int right = -1;
	if(z->pLeft!=NULL) left = height(z->pLeft);
	if(z->pRight!=NULL) right = height(z->pRight);
	change_height(z, max(left,right)+1);
}

TreeNode * rotateLeft(TreeNode * z){
	rotNum += 1;
	TreeNode * y= z->pRight;
	z->pRight=y->pLeft;
	if(y->pLeft!=NULL) y->pLeft->pParent=z;
	y->pLeft=z;
	z->pParent=y;
	setHeightFromSubtrees(z);
	setHeightFromSubtrees(y);
	return y;
}

TreeNode * rotateRight(TreeNode * z){
	rotNum += 1;
	TreeNode * y = z->pLeft;
	z->pLeft = y->pRight;
	if(y->pRight!=NULL) y->pRight->pParent=z;
	y->pRight = z;
	z->pParent=y;
	setHeightFromSubtrees(z);
	setHeightFromSubtrees(y);
	return y;
}

TreeNode * restructure(TreeNode * x, TreeNode * y, TreeNode * z){
	if ((y==z->pLeft)&&(x==y->pLeft)){
		return rotateRight(z);
	} else if ((y==z->pLeft)&&(x==y->pRight)){
		z->pLeft=rotateLeft(y);
		if(z->pLeft != NULL) z->pLeft->pParent = z;
		return rotateRight(z);
	} else if ((y==z->pRight)&&(x==y->pLeft)){
		z->pRight=rotateRight(y);
		if(z->pRight != NULL) z->pRight->pParent = z;
		return rotateLeft(z);
	} else {
		return rotateLeft(z);
	}
}

class AVLTree :public BST {
private:
public:
	AVLTree();
	~AVLTree();
    TreeNode * insert(int k);
};

AVLTree::AVLTree() {
}

AVLTree::~AVLTree() {
} 

TreeNode * AVLTree::insert(int k) {
	TreeNode * z = BST::insert(k);

	while(z != NULL){
		TreeNode * y = NULL;
		TreeNode * x = NULL;
		// caluculate the difference
		int diff = 0;
		if ((z->pLeft != NULL) && (z->pRight != NULL)){
			diff = height(z->pLeft)-height(z->pRight);
		} else if ((z->pLeft == NULL) && (z->pRight != NULL)){
			diff = -1 - height(z->pRight);
		} else if ((z->pLeft != NULL) && (z->pRight == NULL)){
			diff = height(z->pLeft) - (-1);
		} 
		// if it violate the rule of AVL-tree
		if(abs(diff) > 1){
			// Let y be the taller child of z
			if (diff > 0) y = z->pLeft;
			else y=z->pRight;
			// Let x be the taller child of y 
			int lheight = -1;
			int rheight = -1;
			if (y->pLeft != NULL) lheight = height(y->pLeft);
			if (y->pRight != NULL) rheight = height(y->pRight); 
			if (lheight-rheight>0) x = y->pLeft;
			else x = y->pRight;
			// update new z
			TreeNode * Parent = z->pParent;
			TreeNode * oldz = z;
			// cout << z->key << endl;
			if(z==BST::pRoot) {
				z=restructure(x,y,z);
				BST::pRoot=z;
			} else {
				z=restructure(x,y,z);
			}
			z->pParent=Parent;
			if((Parent!=NULL)&&(oldz==Parent->pLeft)) {
				Parent->pLeft = z;
				// cout << Parent->key << endl;
			}else if ((Parent!=NULL)&&(oldz==Parent->pRight)) {
				Parent->pRight = z;
				// cout << Parent->key << endl;
			}
			break;
		}
		setHeightFromSubtrees(z);
		z=z->pParent;
	}

	return(z);
}

// Helper functions for ScapegoatTree
int get_size(TreeNode * z){
	if(z==NULL) return 0;
	else return z->field;
}

void increase_size_one(TreeNode * z){
	z->field += 1;
}

vector<int> get_vector(TreeNode * z){
	std::vector<int> result;
	std::vector<int> left;
	std::vector<int> right;
	if (z==NULL) {
		return result;
	} else {
		result.push_back(z->key);
		if(z->pLeft!=NULL){
			left=get_vector(z->pLeft);
			result.insert(result.begin(),left.begin(),left.end());
		}
		if(z->pRight!=NULL){
			right=get_vector(z->pRight);
			result.insert(result.end(), right.begin(), right.end());
		}
		return result;
	}
	
	
}

TreeNode * reBuild(vector<int> & v, int start, int last){
	if(start > last){
		return NULL;
	} else {
		TreeNode * pNewNode = new TreeNode();
		int middle = (start+last)/2;
		pNewNode->key=v[middle];
		pNewNode->field=last-start+1;
		pNewNode->pLeft=reBuild(v,start, middle-1);
		if(pNewNode->pLeft!=NULL) pNewNode->pLeft->pParent=pNewNode;
		pNewNode->pRight=reBuild(v,middle+1,last);
		if(pNewNode->pRight!=NULL) pNewNode->pRight->pParent=pNewNode;
		return pNewNode;
	}
}


// class ScapegoatTree
class ScapegoatTree :public BST {
private:
public:
	ScapegoatTree();
	~ScapegoatTree();
        TreeNode * insert(int k);
};

ScapegoatTree::ScapegoatTree() {
}

ScapegoatTree::~ScapegoatTree() {
}

TreeNode * ScapegoatTree::insert(int k) {
	TreeNode * z = BST::insert(k);
	z->field=1;
	// your code to update the structure goes here
	stack<TreeNode *> S;

	// Use a stack to store all of its parent
	while(z->pParent!=NULL){
		increase_size_one(z->pParent);
		S.push(z->pParent);
		z=z->pParent;
	}

	// Check condition going downward
	while(S.size()>=2){
		TreeNode * p = S.top();
		S.pop();
		if(2*get_size(p)<3*max(get_size(p->pLeft),get_size(p->pRight))){
			TreeNode * OldParent = p->pParent;
			TreeNode * Oldp = p;
			vector<int> v = get_vector(p);
			if(p==BST::pRoot) {
				int size = v.size();
				// cout << "the size is " << size;
				p=reBuild(v,0,size-1);
				BST::pRoot=p;
			} else {
				p=reBuild(v,0,v.size()-1);
				if(OldParent->pLeft==Oldp){
					OldParent->pLeft=p;
				} else {
					OldParent->pRight=p;
				}
			}
			p->pParent=OldParent;
			z=p;
			break;
		}
	}

	return(z);
}

class MTFTree :public BST {
private:
public:
	MTFTree();
	~MTFTree();

        TreeNode * insert(int k);
};

MTFTree::MTFTree() {
}

MTFTree::~MTFTree() {
}

TreeNode * MTFTree::insert(int k) {
	TreeNode * z = BST::insert(k);

	// your code to update the structure goes here
	TreeNode * y = z->pParent;
	while(y!=NULL){
		TreeNode * GrandParent = y->pParent;
		if (z==y->pLeft){
			z=rotateRight(y);
		} else {
			z=rotateLeft(y);
		}
		z->pParent=GrandParent;
		if(GrandParent!=NULL){
			if(y==GrandParent->pLeft) GrandParent->pLeft=z;
			if(y==GrandParent->pRight) GrandParent->pRight=z;
		}
		y=z->pParent;
	}

	// The root is z(z.parent is NULL)
	BST::pRoot=z;

	return(z);
}


class SplayTree :public BST {
private:
public:
	SplayTree();
	~SplayTree();
        TreeNode * insert(int k);
};

SplayTree::SplayTree() {
}

SplayTree::~SplayTree() {
}

TreeNode * SplayTree::insert(int k) {
	TreeNode * z = BST::insert(k);

	// your code to update the structure goes here
	while((z->pParent!=NULL)&(z->pParent->pParent!=NULL)){
		TreeNode * p = z->pParent;
		TreeNode * g = p->pParent;
		TreeNode * OldParent = g->pParent;
		if((p==g->pLeft)&&(z==p->pLeft)){
			p=rotateRight(g);
			p->pParent=OldParent;
			z=rotateRight(p);
		} else if((p==g->pLeft)&&(z==p->pRight)){ 
			g->pLeft=rotateLeft(p);
			g->pLeft->pParent=g;
			z=rotateRight(g);
		} else if((p==g->pRight)&&(z==p->pLeft)){
			g->pRight=rotateRight(p);
			g->pRight->pParent=g;
			z=rotateLeft(g);
		} else {
			p=rotateLeft(g);
			p->pParent=OldParent;
			z=rotateLeft(p);
		}

		// update the relationship with Oldparent
		z->pParent=OldParent;
		if(OldParent!=NULL){
			if(g==OldParent->pLeft) OldParent->pLeft=z;
			else OldParent->pRight=z;
		}
	}

	if(z->pParent != NULL){
		if(z==z->pParent->pLeft){
			z=rotateRight(z->pParent);
			z->pParent=NULL;
		} else {
			z=rotateLeft(z->pParent);
			z->pParent=NULL;
		}
	}

	// The root is z(z.parent is NULL)
	BST::pRoot=z;

	return(z);
}

// Please leave the following "#ifndef" lines in place; this is needed
// for the cs240 test scripts to run correctly.

#ifndef TESTING
int main() {
	cout << "Start testing for AVL Tree" << endl;
    AVLTree * myAVLTree = new AVLTree();
  	// 4,6,2,1,7,0,5,3
    myAVLTree->insert(20);
    myAVLTree->insert(4);
    myAVLTree->insert(6);
    myAVLTree->insert(12);
    myAVLTree->insert(24);
    myAVLTree->insert(16);
    myAVLTree->insert(13);
    myAVLTree->insert(29);
    myAVLTree->insert(8);
    myAVLTree->insert(2);
    myAVLTree->insert(19);
    myAVLTree->insert(1);
    myAVLTree->insert(7);
    myAVLTree->insert(30);
    myAVLTree->insert(17);
    myAVLTree->insert(23);

    myAVLTree->insert(31);
    myAVLTree->insert(14);
    myAVLTree->insert(9);
    myAVLTree->insert(18);
    myAVLTree->insert(28);
    myAVLTree->insert(15);
    myAVLTree->insert(0);
    myAVLTree->insert(21);
    myAVLTree->insert(11);
    myAVLTree->insert(27);
    myAVLTree->insert(5);
    myAVLTree->insert(10);
    myAVLTree->insert(22);
    myAVLTree->insert(25);
    myAVLTree->insert(26);


	cout << "Number of rotations is " << rotNum << endl;
	
    // myAVLTree->insert(45);
    // myAVLTree->insert(46);
    // myAVLTree->insert(43);
    // myAVLTree->insert(41);
    // myAVLTree->insert(44);
    // myAVLTree->insert(42);
    // myAVLTree->insert(15);
    // myAVLTree->insert(28);
    // myAVLTree->insert(26);
    // myAVLTree->insert(24);
    // myAVLTree->insert(34);
    // myAVLTree->insert(37);
    // myAVLTree->insert(38);
	// myAVLTree->preOrder(); // 40 30 20 15 10 26 24 28 35 34 37 38 50 43 41 42 45 44 46 60 70
	// myAVLTree->inOrder(); // 10 15 20 24 26 28 30 34 35 37 38 40 41 42 43 44 45 46 50 60 70
    myAVLTree->print();
	delete myAVLTree;
	}		
#endif
