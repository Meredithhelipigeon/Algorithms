class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        numbers=[]
        ops=[]
        
        curNums=[]
        for e in expression:
            if '0'<=e<='9':
                curNums.append(e)
            else:
                numbers.append(int(''.join(curNums)))
                curNums=[]
                ops.append(e)
        numbers.append(int(''.join(curNums)))
        
        dp = [[[] for i in range(len(numbers))] for j in range(len(numbers))]
        def calculater_helper(i,j):
            if len(dp[i][j])!=0:
                return dp[i][j]
            if j-i==0:
                dp[i][j]=[numbers[i]]
                return dp[i][j]
            ret = []
            for k in range(i,j):
                s1 = calculater_helper(i,k)
                s2 = calculater_helper(k+1,j)
                for part1 in s1:
                    for part2 in s2:
                        cur = 0
                        if ops[k]=='+':
                            cur=part1+part2
                        elif ops[k]=='-':
                            cur=part1-part2
                        else:
                            cur=part1*part2
                        ret.append(cur)
            dp[i][j]=ret
            return ret
        
        calculater_helper(0,len(numbers)-1)
        return list(dp[0][-1])
