class Solution(object):
    def sortArrayByParityII(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        odd=[]
        even=[]
        
        for i in range(len(nums)):
            if not i%2 == nums[i]%2:
                if i%2==1:
                    if len(even)==0:
                        odd.append(i)
                    else:
                        p=even.pop()
                        temp=nums[p]
                        nums[p]=nums[i]
                        nums[i]=temp
                else:
                    if len(odd)==0:
                        even.append(i)
                    else:
                        p=odd.pop()
                        temp=nums[p]
                        nums[p]=nums[i]
                        nums[i]=temp
        return nums
