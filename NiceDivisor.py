class Solution(object):
        Owndict={}
        def maxNiceDivisors(self, primeFactors):
            """
            :type primeFactors: int
            :rtype: int
            """
            if primeFactors==1 :
                return 1
            
            i = 1
            currentMax = 0
            while i<=primeFactors/2 :
                x = max(self.maxNiceDivisors(i),i)
                y = max(self.maxNiceDivisors(primeFactors-i),primeFactors-i)
                current = x*y
                if current > currentMax:
                    currentMax = current
                i+=1
            
            return currentMax

        def maxNiceDivisorsV2(self, primeFactors):
            """
            :type primeFactors: int
            :rtype: int
            """
            if primeFactors==1 :
                return 1
            
            if self.Owndict.get(primeFactors)!=None :
                return max(self.Owndict[primeFactors]%1000000007, primeFactors)
            i = 1
            currentMax = 0
            while i<=primeFactors/2 :
                x = 0
                y = 0
                if self.Owndict.get(i) == None:
                    x = self.maxNiceDivisors(i)
                    x=max(i,x)
                else:
                    x = max(self.Owndict[i],i)
                if self.Owndict.get(primeFactors-i) == None:
                    y = self.maxNiceDivisors(primeFactors-i)
                    y=max(y,primeFactors-i)
                else:
                    y = max(self.Owndict[primeFactors-i],primeFactors-i)
                current = x*y
                if current > currentMax:
                    currentMax = current
                i+=1
                
            self.Owndict[primeFactors] = currentMax
            return max(currentMax%1000000007,primeFactors)

        def maxNiceDivisorsV3(self, primeFactors):
            """
            :type primeFactors: int
            :rtype: int
            """
            k3=0
            if primeFactors%3 == 1:
                k3 = max(primeFactors/3 - 1, 0)
            else:
                k3 = primeFactors/3
            k2 = (primeFactors-k3*3)/2
            ans = 1
            trans = k3
            method = []
            while k3 > 1:
                if k3 % 2 == 1:
                    method.append('+')
                method.append('*')
                k3 /= 2
            if trans > 0:
                ans = 3
            while len(method)>0:
                l = method.pop()
                if l == '+':
                    ans *= 3
                else:
                    ans = ans * ans
                ans %= 1000000007
                
            while k2 > 0:
                ans *= 2
                k2 -= 1
            return ans%1000000007

