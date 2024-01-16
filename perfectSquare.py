def perfectSquare(num):
    for i in range (2, num//2):
        if (i* i == num):
            return True
    return False


print(perfectSquare(121))