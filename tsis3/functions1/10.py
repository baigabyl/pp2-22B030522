def unique(mylist):
    uni =[]
    for i in range(len(mylist)):
        for j in range(len(mylist)):
            if mylist[i] == mylist[j] and i !=j:
                mylist[j] = "De1ete it"
    for i in range(len(mylist)):
        if mylist[i] == "De1ete it": continue
        uni.append(mylist[i])
    return uni

mylist = ['a','s', 'd', 'f', 'a', 'e', 'e']
print(unique(mylist))
    
