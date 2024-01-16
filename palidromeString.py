def paliString(s):
    i =0
    j = len(s) -1
    while(i< j):
        if s[i] != s[j]:
            return "Not a Palidrome"
        i+=1
        j-=1
        
    return "Palidrome"

print(paliString("abc=cba"))