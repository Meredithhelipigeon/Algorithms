def combine_2dasher(d1,d2):
    dp=[[[] for i in range(len(d2)+1)] for j in range(len(d1)+1)]

    for i in range(1,len(d1)+1):
        for j in range(1,len(d2)+1):
            if d1[i-1]==d2[j-1]:
                dp[i][j]=dp[i-1][j-1]+[d1[i-1]]
            else:
                if len(dp[i][j-1])<len(dp[i-1][j]):
                    dp[i][j]=dp[i-1][j]
                else:
                    dp[i][j]=dp[i][j-1]
    
    return dp[-1][-1]

# example 1
d1=["chilis", "albertsons", "walmart", "albertsons", "chilis", "mcdonalds", "burger king"]
d2=["chilis", "walmart", "chilis", "albertsons", "burger king", "applebees", "mcdonalds"]
print(combine_2dasher(d1,d2))

# example 2
d1=["chil‍‌‍‌‍‍‌‍‌‌‌‌‌‌‌‍‍‍‌‍is", "albertsons", "mcdonalds"]
d2=["burger king", "jamba juice", "applebees"]
print(combine_2dasher(d1,d2))

def combine_2dasher_2(d1,d2):
    dp=[[[0,(-1,-1)] for i in range(len(d2)+1)] for j in range(len(d1)+1)]

    for i in range(1,len(d1)+1):
        for j in range(1,len(d2)+1):
            if d1[i-1]==d2[j-1]:
                dp[i][j][0]=dp[i-1][j-1][0]+1
                dp[i][j][1]=(i-1,j-1)
            else:
                if dp[i][j-1][0]<dp[i-1][j][0]:
                    dp[i][j][0]=dp[i-1][j][0]
                    dp[i][j][1]=(i-1,j)
                else:
                    dp[i][j][0]=dp[i][j-1][0]
                    dp[i][j][1]=(i,j-1)
    
    cur=(-1,-1)
    ret=[]
    while dp[cur[0]][cur[1]][0] > 0:
        if d1[cur[0]-1]==d2[cur[1]-1]:
            ret.append(d1[cur[0]-1])
        cur=dp[cur[0]][cur[1]][1]

    return list(reversed(ret))

# example 1
d1=["chilis", "albertsons", "walmart", "albertsons", "chilis", "mcdonalds", "burger king"]
d2=["chilis", "walmart", "chilis", "albertsons", "burger king", "applebees", "mcdonalds"]
print(combine_2dasher_2(d1,d2))

# example 2
d1=["chil‍‌‍‌‍‍‌‍‌‌‌‌‌‌‌‍‍‍‌‍is", "albertsons", "mcdonalds"]
d2=["burger king", "jamba juice", "applebees"]
print(combine_2dasher_2(d1,d2))