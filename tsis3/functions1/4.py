def primeOnly(a):
    prime = []
    for i in a:
        temp = True
        for j in range(2, int(i)):
            if (int(i) % (j)) == 0:
                temp = False
                break      
        if temp:
          prime.append(i)
    return prime

a = [1, 2, 3, 4, 5, 6]
print(primeOnly(a))