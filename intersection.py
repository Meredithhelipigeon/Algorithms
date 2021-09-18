class Solution1(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        nums1=sorted(nums1)
        nums2=sorted(nums2)
        
        ret=[]
        i1=0
        i2=0
        while i1 < len(nums1) and i2 < len(nums2):
            if nums1[i1] == nums2[i2]:
                ret.append(nums1[i1])
                i1+=1
                i2+=1
            else:
                if nums1[i1] < nums2[i2]:
                    i1+=1
                else:
                    i2+=1
        return ret

class Solution2(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        hash_map=[0]*1001
        
        for n in nums1:
            hash_map[n]+=1
        
        ret=[]
        
        for n in nums2:
            if hash_map[n]>=1:
                ret.append(n)
                hash_map[n]-=1
        
        return ret