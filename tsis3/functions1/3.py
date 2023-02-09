def solve(numheads, numlegs):
    for i in range(numheads):
        if (2*(i+1) + 4*(numheads-(i+1))) == numlegs:
            return i+1
        if (2*(numheads-(i+1)) + 4*(i+1)) == numlegs:
            return i+1
    return "NOT CORRECT INPUT"

print("count of heads")
numheads = int(input())
print("count of legs")
numlegs = int(input())


s = solve(numheads, numlegs)
if type(s) != type("qw"):
    if (2*s + 4*(numheads-s)) == numlegs:
      chi = int(s)
      rab = numheads - chi
      print("Rabbit:", rab, "Chicken:", chi  )
    else:
      rab = int(s)
      chi = numheads - rab
      print("Rabbit:", rab, "Chicken:", chi  )

else:
   print(s)