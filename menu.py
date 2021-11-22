def menus(oldMenu,newMenu)
    def count(n):
        if n==None:
            return 0
        ret=1
        for c in n.children:
            ret+=count(c)
        return ret
        
    def find_children(oldCur,newCur):
        oldDict={}
        newDict={}
        for oc in oldCur.children:
            oldDict[oc.key]=oc
        for nc in newCur.children:
            newDict[nc.key]=nc
        oldKeySet=set(oldDict.keys())
        newKeySet=set(newDict.keys())
        intersect=oldKeySet & newKeySet
        for k in intersect:
            if oldDict[k].val==newDict[k].val:
                find_children(oldDict[k],newDict[k])
            else:
                count(oldDict[k],newDict[k])
        for ok in oldKeySet-intersect:
            diff += count(oldDict[ok])
        for nk in newKeySet-intersect:
            diff += count(newDict[ok])    

    diff=0
    if oldMenu and newMenu and oldMenu.key==newMenu.key and oldMenu.children==newMenu.children:
        find_children(oldMenu,newMenu)
    else:
        diff += count(oldMenu)
        diff += count(newMenu)

