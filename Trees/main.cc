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

