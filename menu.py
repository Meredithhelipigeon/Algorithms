# At DoorDash, menus are updated daily even hourly to keep them up-to-date. Each menu can be regarded as a tree. When the merchant sends us the latest menu, can we calculate
# how many nodes have changed/added/deleted?

# Assume each Node structure is as below:

# class Node {
#         String key;
#         int value;
#         List<Node> children;
# }

# Assume there are no duplicate nodes with the same key.

# Output: Return the number of changed nodes in the tree.

#             Existing tree
#                a(1)
#             /       \
#          b(2)      c(3)
#         /     \         \
#       d(4)    e(5)      f(6)


#             New tree
#             a(1)
#                 \
#                c(3)
#                    \
#                    f(66)

# a(1) a is the key, 1 is the value
# For example, there are a total of 4 changed nodes. Node b, Node d, Node e are automatically set to inactive. The value of Node f changed as well.


#           Existing tree
#             a(1)
#           /       \
#         b(2)      c(3)
#       /       \       \
#   d(4)      e(5)      g(7)


#               New tree
#                 a(1)
#             /          \
#          b(2)         h(8)
#       /    |   \           \
# e(5)   d(4)   f(6)       g(7)


# There are a total of 5 changed nodes. Node f is a newly-a‍‌‍‌‍‍‌‍‌‌‌‌‌‌‌‍‍‍‌‍dded node. c(3) and old g(7) are deactivated and h(8) and g(7) are newly added nodes


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

