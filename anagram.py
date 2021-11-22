def find_swap_1(r,rlist):
    ret=[]
    for other_r in rlist:
        if len(other_r)!=len(r):
            continue
        swapIndex=[]
        judge=True
        for i in range(len(r)):
            if r[i]!=other_r[i]:
                if len(swapIndex)<2:
                    swapIndex.append(i)
                else:
                    judge=False
                    break
        if len(swapIndex)==1 or (len(swapIndex)==2 and (not other_r[swapIndex[0]]==r[swapIndex[1]] and other_r[swapIndex[1]]==r[swapIndex[0]])):
            judge=False
        if judge:
            ret.append(other_r)
    return ret

print(find_swap_1("five guys",["five ugsy", "fiee guys", "eivf guys"]))

def find_swap_k(r,rlist,k):
    ret=[]

    for other_r in rlist:
        if len(other_r)!=len(r):
            continue
        nameListMap=[0]*26
        for i in range(len(r)):
            if r[i]==' ' and other_r[i]==' ':
                continue
            nameListMap[ord(r[i])-ord('a')]+=1
            nameListMap[ord(other_r[i])-ord('a')]-=1
        addNum=0
        for diff in nameListMap:
            if diff>0:
                addNum+=diff
        print(addNum)
        if addNum<=k:
            ret.append(other_r)
    return ret

print(find_swap_k("five guys",["five kkkk", "fiee guys", "eivf kkys"],2))