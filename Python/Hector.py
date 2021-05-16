l = [[1,2],[1,0],[2,1]]
l1 = sorted(l, key=lambda x: (-x[0], x[1]))
print(l1)

def word_hash_value(w,R,M):
    h = 0
    for i in range(len(w)):
        h = h * R
        h = h + ord(w[i])
        h = h % M
    return h


print(word_hash_value("stop",129,128))
print(word_hash_value("post",129,128))
print(word_hash_value("pots",129,128))

List_1 = [0,1]
List_2 = [0,0]

print(List_1==List_2)

