def histogram(mylist):
    for i in mylist:
        for j in range(int(i)):
            print("*", end = "")
        if i != mylist[len(mylist)-1]: print()
    return ""

print(histogram([4, 9, 7]))