def guess(min, max, guessed, num):
    if num < guessed: print("Your guess is too low.")
    if num > guessed: print("Your guess is too high.")
    print("Take a guess")
    return 0
    


print("what is your guessed number")
guessed = int(input())
print("print your lower num")
min = input()
print("print your higer num")
max = int(input())

print("Hello! What is your name?")
name = (input())
qwe = ("Well, {}, I am thinking of a number between {} and {}.")
print(qwe.format(name, min, max))
print("Take a guess")

cnt =0
temp = True
while(temp):
    cnt +=1
    num = int(input())
    if(num == guessed):
        fin = ("Good job, {}! You guessed my number in {} guesses!")
        print(fin.format(name,cnt))
        temp = False
        break
    guess(min, max, guessed, num)