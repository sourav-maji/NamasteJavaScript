def checkPalidrome(num):
    res = 0
    new_no= num;
    while(num >0):
        res=(res *10) +  num%10
        num//=10
        print(res)
    print(f"Result : {res}")
    if(new_no == res ):
        print("Palidrome")
    else:
        print("Not Palidrome")


checkPalidrome(121)