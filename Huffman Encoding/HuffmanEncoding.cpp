/* compile with g++ -std=c++17 -Wall file.cpp*/

#include <iostream>
#include <string>
#include <cmath>
#include <queue> 
#include <vector> 

class Trie {
	public:
	std::vector<Trie*> dway;
	Trie* parent;
	int plink=0;
	bool isLeaf;
	int frequencies;

	// Constructor
	Trie(int d, bool isLeaf = false, int frequencies = 0);
	// Destructor
	~Trie() { 
		for(auto s: dway){
			delete s;
		}
	}
};

Trie::Trie(int d, bool isLeaf, int frequencies) {
	this->isLeaf=isLeaf;
	if (isLeaf) {
		this->frequencies=frequencies;
		this->parent=nullptr;
	} else {
		for(int i = 0;i<d;i++){
			this->dway.push_back(nullptr);
		}
		this->parent=nullptr;
	}
}


// Helper Function
Trie* build_trie(std::vector<Trie*> T){
	Trie* BigTrie= new Trie(T.size());
	int sumFreq=0;
	int size = T.size();
	for(int i = 0;i<size;++i){
		BigTrie->dway[i]=T[i];
		T[i]->parent=BigTrie;
		T[i]->plink=i;
		sumFreq+=T[i]->frequencies;
	}
	// update the frequencies for the combined trie
	BigTrie->frequencies= sumFreq;
	return BigTrie;
}

// print_trie(root) is only used for debug
void print_trie(Trie * root){
	if(root!=nullptr){
		std::cout << root->frequencies << " ";
		for(auto t: root->dway){
			print_trie(t);
		}
	}
}

class HuffmanEncoding {
        public:
                HuffmanEncoding() { }
                ~HuffmanEncoding() { 
					delete root;
				}

		std::string getCodeWord(char c);
		std::string dWayEncoding(std::string S, int d);

		// add methods/fields here as needed
	private:
	void buildTrie(std::vector<int>, int d);
	Trie* root;
	std::vector<Trie*> EncodeList;
};

struct compare  
 {  
   bool operator()(const Trie*  l, const Trie*  r)  
   {  
       return l->frequencies >= r->frequencies;  
   }  
 };

void HuffmanEncoding::buildTrie(std::vector<int> f, int d) {
	std::priority_queue<Trie*,std::vector<Trie*>,compare> Q;
	std::vector<Trie*> OurEncodeList(95,nullptr);
	this->EncodeList=OurEncodeList;
	// turn frequency queue to single node
	int size = f.size();
	for(int i = 0;i < size;++i){
		if(f[i]>0){
			Trie* single = new Trie(d,true,f[i]);
			EncodeList[i]=single;
			Q.push(single);
		}
	}

	// build encoding trie
	while(Q.size()>1){
		int size=Q.size();
		int k=std::min(d,size);
		std::vector<Trie*> T;
		for(int i = 0;i < k;++i){
			T.push_back(Q.top());
			Q.pop();
		}
		Trie* BigTree=build_trie(T);
		Q.push(BigTree);
	}

	// Set root
	if (Q.top()->isLeaf) {
		std::vector<Trie*> T;
		T.push_back(Q.top());
		root = build_trie(T);
	} else {
		root=Q.top();
	}
	Q.pop();
}


std::string HuffmanEncoding::getCodeWord(char c) {
// pre: buildEncodingTrie(T,d) has been called earlier, c is between 32 and 126
// post: returns code-word for char c, if c appears in T, and empty string otherwise
	std::string w = "";
	// find the leaf for this character
	Trie* leaf=EncodeList[c-32];
	// Use the trie to get the string
	if (leaf!=nullptr){
		while(leaf->parent!=nullptr){
			char c = leaf->plink+48;
			w.insert(w.begin(),c);
			leaf=leaf->parent;
		}
	}

	return w;
}

std::string  HuffmanEncoding::dWayEncoding(std::string S, int d) {
// pre: S contains ASCII characters between 32 and 126, 2 <= d <= 10
// post: returns d-way Huffman encoding of S
	std::string C = "";
	delete root;
	root=nullptr;

	// initialize frequency array
	std::vector<int> f(95,0);
	// compute frequencies
	for(auto c: S){
		f[c-32]+=1;
	}
	buildTrie(f,d);
	for(auto s: S){
		C.append(getCodeWord(s));
	}
	
	return C;
}



// please leaving the following "ifndef" in place for the marking scripts
#ifndef TESTING
int main() {
	std::string S = "'Well, that's what I am going to do, too,' said the bad little pumpkin vine, 'all but the pies; but I'm not going to stay here to do it. I'm going to that fence over there, where the morning-glories were last summer, and I'm going to show them what a pumpkin-glory is like. I'm just going to cover myself with blossoms; and blossoms that won't shut up, either, when the sun comes out, but 'll stay open, as if they hadn't anything to be ashamed of, and that won't drop off the first day, either. I noticed those morning-glories all last summer, when I was nothing but one of the blossoms myself, and I just made up my mind that as soon as ever I got to be a vine, I would show them a thing or two. Maybe I can't be a morning-glory, but I can be a pumpkin-glory, and I guess that's glory enough.'";
    HuffmanEncoding * h = new HuffmanEncoding;

	std::string C = h->dWayEncoding(S,2);
	int base = log2(2.0)*C.length();

	for(int d = 2;d<11;++d){
		std::string C = h->dWayEncoding(S,d);
		std::cout << d << "-way encoding of " <<  " is " << " with length " << C.length() << " and cost " << log2(d)*C.length() << " ratio " << log2(d)*C.length()*100/base << "\n";
	}
	

    delete h;
}
#endif