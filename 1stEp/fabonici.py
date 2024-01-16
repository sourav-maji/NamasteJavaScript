def fabonici(n):
    if n < 0:
        return "Invalid Input"
    elif n== 0 or n== 1 or n== 2:
        return n
    else:
        return fabonici(n-1 ) + fabonici(n-2)
    
userInput = int(input("Enter the Number "))

print(fabonici(userInput))


l= [1,2,3,4]
l.insert(2,5)
print(l)
l.remove(3)
l.pop()
# del l  this will delete the list l


a = ("harry","shiv", "Suvam")
print(type(a))
print(a[0])
print(len(a))