class Solution:
    # Hash table "One word one set"
    # m: max length of word, n: len of words
    # time complexity: O(m*n)
    def maxProduct(self, words: List[str]) -> int:
        commenSets = []
        
        # Step 1. Create hash table word_to_set
        for w in words:
            curSet=set()
            for alpha in w:
                curSet.add(alpha)
            commenSets.append(curSet)
        
        # Step 2. Find the maximum product of word Length
        ret=0
        for i in range(len(words)):
            for j in range(i+1,len(words)):
                if len(commenSets[i].intersection(commenSets[j]))==0:
                    ret=max(ret,len(words[i])*len(words[j]))

        return ret
