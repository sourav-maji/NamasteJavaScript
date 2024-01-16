def checkPrime(num):
    for i in range(2, num//2):
        if (num %i == 0):
            return "Not Prime"
    
    return "Prime"


print(checkPrime(41))