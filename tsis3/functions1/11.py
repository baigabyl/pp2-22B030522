def polindrome(word):
    l = len(word)
    for i in range(l):
        if word[i] != word[l-i-1]: return False
        if l/2 > i: return True

word = "madam"
print(polindrome(word))
print(polindrome("miss"))
print(polindrome("mm"))