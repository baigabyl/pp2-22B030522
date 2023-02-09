def reverse(s):
    rev = ""
    s = s.split(" ")
    cnt =-1
    for i in s:
        rev += " " +(s[cnt])
        cnt -= 1
    return rev.strip()

s = str(input())
print(reverse(s))