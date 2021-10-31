class RandomizedSet(object):

    def __init__(self):
        self.randomDic={}
        self.randomList=[]

    def insert(self, val):
        """
        :type val: int
        :rtype: bool
        """
        if val in self.randomDic and not self.randomDic[val]==-1 :
            return False
        else:
            self.randomDic[val]=len(self.randomList)
            self.randomList.append(val)
            return True
            

    def remove(self, val):
        """
        :type val: int
        :rtype: bool
        """
        if val in self.randomDic and not self.randomDic[val]==-1:
            self.randomList[self.randomDic[val]]=self.randomList[-1]
            self.randomDic[self.randomList[-1]]=self.randomDic[val]
            self.randomList.pop()
            self.randomDic[val]=-1
            return True
        else:
            return False

    def getRandom(self):
        """
        :rtype: int
        """
        index=random.randint(0,len(self.randomList)-1)
        return self.randomList[index]
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
