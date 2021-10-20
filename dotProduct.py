class SparseVector:
    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.nums=set()
        self.realNums=nums
        for index,num in enumerate(nums):
            if num>0:
                self.nums.add(index)
        

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec):
        """
        :type vec: 'SparseVector'
        :rtype: int
        """
        ret=0
        for key in vec.nums & self.nums:
            ret+=vec.realNums[key]*self.realNums[key]
        return ret
        

# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)
