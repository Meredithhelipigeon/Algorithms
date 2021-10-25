class RandomizedSet(object):

    def __init__(self):
        self.randomSet=set()

    def insert(self, val):
        """
        :type val: int
        :rtype: bool
        """
        if val in self.randomSet:
            return False
        else:
            self.randomSet.add(val)
            return True
            

    def remove(self, val):
        """
        :type val: int
        :rtype: bool
        """
        if val in self.randomSet:
            self.randomSet.remove(val)
            return True
        else:
            return False

    def getRandom(self):
        """
        :rtype: int
        """
        return random.sample(self.randomSet,1)[0]
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
