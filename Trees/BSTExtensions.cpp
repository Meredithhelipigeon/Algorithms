#include <iostream>
#include <fstream>
#include <random>
#include <math.h>
#include "BST.h"
#include <stack>
#include <vector>

using namespace std;

// Helper functions for AVLTree
int height(TreeNode * z){
	return z->field;
}

// change_height(z, height) will change the height field
void change_height(TreeNode * z, int height){
	z->field = height;
}

// setHeightFromSubtrees(z) updates the right height of the subtrees
void setHeightFromSubtrees(TreeNode * z){
	int left = -1;
	int right = -1;
	if(z->pLeft!=NULL) left = height(z->pLeft);
	if(z->pRight!=NULL) right = height(z->pRight);
	change_height(z, max(left,right)+1);
}

// Rotation Helper Functions
TreeNode * rotateLeft(TreeNode * z){
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
	TreeNode * y = z->pLeft;
	z->pLeft = y->pRight;
	if(y->pRight!=NULL) y->pRight->pParent=z;
	y->pRight = z;
	z->pParent=y;
	setHeightFromSubtrees(z);
	setHeightFromSubtrees(y);
	return y;
}

// restructure(x,y,z) restructures the tree
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
			// If it is the root, set root
			if(z==BST::pRoot) {
				z=restructure(x,y,z);
				BST::pRoot=z;
			} else {
				z=restructure(x,y,z);
			}
			// set parent reference
			z->pParent=Parent;
			if((Parent!=NULL)&&(oldz==Parent->pLeft)) {
				Parent->pLeft = z;
			}else if ((Parent!=NULL)&&(oldz==Parent->pRight)) {
				Parent->pRight = z;
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

// get_vector(z) will return a vector of elements in ascending order
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

// reBuild(v,start,last) rebuilds a tree 
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
			// delete the old tree in case of memory leak
			delete Oldp;
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
	while((z->pParent!=NULL)&&(z->pParent->pParent!=NULL)){
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

	// if there is still one step to the root
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
	// your testing routines go here. 

    // Testings for AVLTree 
    cout << "Start testing for AVL Tree" << endl;
    AVLTree * myAVLTree = new AVLTree();

    myAVLTree->insert(20);
    myAVLTree->insert(30);
    myAVLTree->insert(40);
    myAVLTree->insert(50);
    myAVLTree->insert(60);
    myAVLTree->insert(70);
    myAVLTree->insert(10);
    myAVLTree->insert(35);
    myAVLTree->insert(45);
    myAVLTree->insert(46);
    myAVLTree->insert(43);
    myAVLTree->insert(41);
    myAVLTree->insert(44);
    myAVLTree->insert(42);
    myAVLTree->insert(15);
    myAVLTree->insert(28);
    myAVLTree->insert(26);
    myAVLTree->insert(24);
    myAVLTree->insert(34);
    myAVLTree->insert(37);
    myAVLTree->insert(38);
	myAVLTree->preOrder(); // 40 30 20 15 10 26 24 28 35 34 37 38 50 43 41 42 45 44 46 60 70
	myAVLTree->inOrder(); // 10 15 20 24 26 28 30 34 35 37 38 40 41 42 43 44 45 46 50 60 70
    myAVLTree->print();
	delete myAVLTree;

	// Testings for ScapegoatTree
    cout << "Start testing for Scapegoat Tree" << endl;
    ScapegoatTree * myScapegoatTree = new ScapegoatTree();
    myScapegoatTree->insert(20);
    myScapegoatTree->insert(30);
    myScapegoatTree->insert(40);
    myScapegoatTree->insert(50);
    myScapegoatTree->insert(60);
    myScapegoatTree->insert(70);
    myScapegoatTree->insert(10);
	myScapegoatTree->insert(35);
    myScapegoatTree->insert(45);
    myScapegoatTree->insert(46);
    myScapegoatTree->insert(43);
    myScapegoatTree->insert(41);
    myScapegoatTree->insert(44);
    myScapegoatTree->insert(42);
    myScapegoatTree->insert(15);
    myScapegoatTree->insert(28);
    myScapegoatTree->insert(26);
    myScapegoatTree->insert(24);
    myScapegoatTree->insert(34);
    myScapegoatTree->insert(37);
    myScapegoatTree->insert(38);
	myScapegoatTree->preOrder(); //  40 26 15 10 20 24 34 28 30 35 37 38 50 45 43 41 42 44 46 60 70
	myScapegoatTree->inOrder(); //  10 15 20 24 26 28 30 34 35 37 38 40 41 42 43 44 45 46 50 60 70
    myScapegoatTree->print();
	delete myScapegoatTree;

    // Testing for MTFTree
    cout << "Start testing for MTFTree" << endl;
    MTFTree * myMTFTree = new MTFTree();
    myMTFTree->insert(20);
    myMTFTree->insert(30);
    myMTFTree->insert(40);
    myMTFTree->insert(10);
    myMTFTree->insert(60);
    myMTFTree->insert(70);
	myMTFTree->insert(35);
    myMTFTree->insert(45);
    myMTFTree->insert(46);
    myMTFTree->insert(43);
    myMTFTree->insert(41);
    myMTFTree->insert(44);
    myMTFTree->insert(42);
    myMTFTree->insert(15);
    myMTFTree->insert(28);
    myMTFTree->insert(26);
    myMTFTree->insert(24);
    myMTFTree->insert(34);
    myMTFTree->insert(37);
    myMTFTree->insert(38);
	myMTFTree->inOrder(); // 10 15 20 24 26 28 30 34 35 37 38 40 41 42 43 44 45 46 60 70
	myMTFTree->preOrder(); // 38 37 34 24 15 10 20 26 28 30 35 42 41 40 44 43 46 45 70 60
    myMTFTree->print();
	delete myMTFTree;


    // Testing for SplayTree
    cout << "Start testing for SplayTree" << endl;
    SplayTree * mySplayTree = new SplayTree();

    mySplayTree->insert(20);
    mySplayTree->insert(30);
    mySplayTree->insert(40);
    mySplayTree->insert(50);
    mySplayTree->insert(60);
    mySplayTree->insert(70);
    mySplayTree->insert(10);
	mySplayTree->insert(35);
    mySplayTree->insert(45);
    mySplayTree->insert(46);
    mySplayTree->insert(43);
    mySplayTree->insert(41);
    mySplayTree->insert(44);
    mySplayTree->insert(42);
    mySplayTree->insert(15);
    mySplayTree->insert(28);
    mySplayTree->insert(26);
    mySplayTree->insert(24);
    mySplayTree->insert(34);
    mySplayTree->insert(37);
    mySplayTree->insert(38);
	mySplayTree->inOrder(); //  10 15 20 24 26 28 30 34 35 37 38 40 41 42 43 44 45 46 50 60 70
	mySplayTree->preOrder(); //  38 37 34 26 24 20 15 10 28 30 35 40 42 41 44 43 45 46 50 60 70
    mySplayTree->print();
	delete mySplayTree;
	}		
#endif

