#include <iostream>
#include <math.h>
using namespace std;

// class to compute median while adding and deleting medians

class OnlineMedian {
private:
int *hlo;
int low;
int low_size;
int *hhi; 
int high;
int high_size;

// exchange_node(type, e1, e2) is a function that exchanges the node e1 and e2.
void exchange_node(bool type, int e1, int e2);

//  which_delete_element(type) deletes the first element of the given type tree.
//  	If we want to delete the element in hhi, type is true
//		If we want to delete the element in hlo, type is false
void which_delete_element(bool type);

// who_insert(type,x) insert x to the tree of the given type tree
// 	If type is high, then type = true. If type is low, then type = false.
void who_insert(bool type, int x);

public:
	OnlineMedian();
	~OnlineMedian();

	int size(); 
	void insert(int x);
	int getMedian();
	int deleteMedian();
};

void OnlineMedian::exchange_node(bool type, int e1, int e2) {
	int exchange = 0;
	if (type==true){
		exchange = hhi[e1];
		hhi[e1] = hhi[e2];
		hhi[e2] = exchange;
	} else {
		exchange = hlo[e1];
		hlo[e1] =  hlo[e2];
		hlo[e2] = exchange;
	}
}

//  If we want to delete the element in hhi, type is true
//	If we want to delete the element in hlo, type is false
void OnlineMedian::which_delete_element(bool type){
	// choose destination
	int *des = nullptr;
	int size = 0;
	if(type == true){
		des = hhi;
		high -= 1;
		size = high;
	} else { 
		des = hlo;
		low -= 1;
		size = low;
	}

	// delete item
	des[0]=des[size];
	des[size]=0;

	// step by step exchange
	int i = 0;
	// left child is 2*i + 1, right child is 2*i + 2
	while(1){
		int child_max = 0;
		int child_min = 0;
		// dir is true if target child is left.
		bool dir = true;
		// determine the child max and the direction
        if(2*i+1 < size){
			if(2*i+2<size){
				if(des[2*i+1]<des[2*i+2]){
					child_max=des[2*i + 2];
					child_min=des[2*i+1];
					if(type) dir = true;
					else dir = false;
				} else {
					child_max=des[2*i + 1];
					child_min=des[2*i+2];
					if(type) dir = false;
					else dir = true;
				}
			} else {
				child_max=des[2*i + 1];
				child_min=des[2*i + 1];
				dir = true;
			}
		} else break;

		// exchange
		if(((child_max>des[i])&&(type==false))||
		   ((child_min<des[i])&&(type==true)))  {
			if(dir){
				exchange_node(type, i, 2*i+1);
				i = 2*i+1;
			} else{
				exchange_node(type, i, 2*i+2);
				i = 2*i+2;
			}	
		} else {
			break;
		}
	}
}

void OnlineMedian::who_insert(bool type, int x){
	// know the destination
	int *des = nullptr;
	int size = 0;
	if(type == true){
		des = hhi;
		high += 1;
		size = high;
	} else { 
		des = hlo;
		low += 1;
		size = low;
	}

    // resize if needed
    if((type==true)&&(size>=high_size)){
		int doublenum = 0;
		if(high_size!=0) doublenum=2*high_size;
		else doublenum=1;
		int *newdes= new int[doublenum];
		for(int i=0;i<high_size;++i){
			newdes[i]=des[i];
		}
		des = newdes;
		delete [] hhi;
		hhi = newdes;
		high_size = doublenum;
	}

	if((type==false)&&(size>=low_size)){
		int doublenum = 0;
		if(low_size!=0) doublenum=2*low_size;
		else doublenum=1;
		int *newdes= new int[doublenum];
		for(int i=0;i<low_size;++i){
			newdes[i]=des[i];
		}
		des = newdes;
		delete [] hlo;
		hlo = newdes;
		low_size = doublenum;
	}
    
	// insert into the last position
    des[size-1]=x;

	// exchange step by step
	int i = size-1;
	while(((type==false)&&(i!=0)&&(des[(i-1)/2]<des[i]))||
	      ((type==true)&&(i!=0)&&(des[(i-1)/2]>des[i]))){
			  exchange_node(type, i,(i-1)/2);
			  i = (i-1)/2;
	}
}

OnlineMedian::OnlineMedian(): hlo {nullptr}, low{0}, low_size{0}, hhi{nullptr}, high{0}, high_size{0} {
// post: initializes empty structure
}

OnlineMedian::~OnlineMedian() {
	delete [] hhi;
	delete [] hlo;
}

int OnlineMedian::size() {
// post: returns number of items in the structure
   return high + low;
}

void OnlineMedian::insert(int x) {
	// pre: x is different from all items in the structure
	if(high+low > 0){
		if(x<hlo[0]){
				if(low>high){
					int newin = hlo[0];
					which_delete_element(false);
					who_insert(true, newin);
					who_insert(false, x);
				} else who_insert(false, x);
		} else if((x>hlo[0])&&(high==0) ){
			who_insert(true,x);
		} else if(x<hhi[0]){
			if(low>high) who_insert(true, x);
			else who_insert(false,x);
		} else {
				if(low>high) who_insert(true,x);
				else{
					int newin = hhi[0];
					which_delete_element(true);
					who_insert(false, newin);
					who_insert(true, x);
				}
		}
	} else {
		who_insert(false, x);
	}
// post: x is stored in the structure
}


int OnlineMedian::getMedian() {
// pre: size > 0
// post: returns median of all inserted numbers
return hlo[0];
}


int OnlineMedian::deleteMedian() {
// pre: size > 0
int item = hlo[0];
which_delete_element(false);
if(high>low){
   int newin = hhi[0];
   which_delete_element(true);
   who_insert(false, newin);
}
return item;
// post: deletes and returns median of all inserted numbers
}

// Please leave the following "#ifndef" lines in place; this is needed
// for the cs240 test scripts to run correctly.

#ifndef TESTING
int main() {
// your testing routines go here.  

	OnlineMedian * h = new OnlineMedian();

	h->insert(15);
	cout << "Receive 15" << endl;
	cout << "Current median is " << h->getMedian() << endl;
	cout << "Delete median: " << h->deleteMedian() << endl;
	h->insert(15);
	cout << "Receive 15" << endl;
	cout << "Current median is " << h->getMedian() << endl;
	h->insert(10);
	cout << "Receive 10" << endl;
	cout << "Current median is " << h->getMedian() << endl;
	h->insert(1);
	cout << "Receive 1" << endl;
	cout << "Current median is " << h->getMedian() << endl;
	h->insert(20);
	cout << "Receive 20" << endl;
	cout << "Current median is " << h->getMedian() << endl;
	h->insert(30);
	cout << "Receive 30" << endl;
	cout << "Current median is " << h->getMedian() << endl;
	h->insert(50);
	cout << "Receive 50" << endl;
	cout << "Current median is " << h->getMedian() << endl;
	h->insert(17);
	cout << "Receive 17" << endl;
	cout << "Current median is " << h->getMedian() << endl;
	h->insert(-5);
	cout << "Receive -5" << endl;
	cout << "Current median is " << h->getMedian() << endl;
	cout << "The size of the array is " << h->size() << endl;
	cout << "Delete median: " << h->deleteMedian() << endl;
	cout << "The size of the array is " << h->size() << endl;
	cout << "Current median is " << h->getMedian() << endl;
	cout << "Delete median: " << h->deleteMedian() << endl;
	cout << "The size of the array is " << h->size() << endl;
	cout << "Current median is " << h->getMedian() << endl;
	h->insert(25);
	cout << "Receive 25" << endl;
	cout << "Current median is " << h->getMedian() << endl;
	cout << "Delete median: " << h->deleteMedian() << endl;
	cout << "Delete median: " << h->deleteMedian() << endl;
	cout << "Delete median: " << h->deleteMedian() << endl;
	cout << "Delete median: " << h->deleteMedian() << endl;
	cout << "Delete median: " << h->deleteMedian() << endl;
	cout << "Delete median: " << h->deleteMedian() << endl;
	cout << "Delete median: " << h->deleteMedian() << endl;

	// you should get 15 here
	delete h;
}
#endif
