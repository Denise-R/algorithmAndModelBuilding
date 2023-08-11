def eachFactor(list, list2):
    listMax = []
    listMin = []
    # list2 = [a,b,c,d,e,f,g]
    # list2 = ['a','b','c','d','e','f','g']

    for i in range(5):
        valueMin = min(list2)
        indices = [i for i, x in enumerate(list) if x == valueMin]
        print(indices)
        ls = [[]]
        for i in indices:
            ls.append([list[indices[i]], list2[i]])
        print(ls)
        print(i)
        if len(ls) == 6 or len(ls) > 6:
            return ls
    #     for i in range(count):
    #         listMin.append(valueMin)
    #     list2 = [ele for ele in list2 if ele != valueMin]
    #     for i in range(count):
    #         listMin.append(valueMin)
    #     if len(listMin) == 5 or len(listMin) > 5:
    #         break
    # return listMin, listMax
list = ['a','b','c','d','e','f','g']
list2 = [1,11,1,-4,1,1,0]
indices = [i for i, x in enumerate(list2) if x == 1]
print(indices)
ls = [[]]
for i in indices:
    ls.append([list[i],list2[i]])
print(ls)

