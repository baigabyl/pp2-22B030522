class onlyprime(object):
    def __init__(self, mylist):
        self.list = mylist
    
    def filter(self):
        prime = []
        for i in range(len(self.list)):
            temp = True
            for j in range(2, int(i)):
              if (int(i) % (j)) == 0:
                temp = False
                break      
            if temp:
              if i != 0 and i !=1:
                prime.append(i)
        return prime

a = [1, 2, 3, 4, 5, 6, 7, 8]
lis = onlyprime(a)
print(lis.filter())