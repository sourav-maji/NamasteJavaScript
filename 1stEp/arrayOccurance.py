def occuranceArray(arr, num):
    count =0
    ocr =[]
    for i in range(0, len(arr)):
        if arr[i] == num:
            print(i+1)
            ocr.append(i)
            count+=1
    print(f"Indexes are : {ocr}")
    return count
numArray = [1,2,3,4,2,5,6,1,7,8,1]
numb= occuranceArray(numArray,1)
print("Occurancy ", numb)


a=42
e = str(a)
print(type(e),e)
name = "   Harry    "
print(name.strip())
print(len(name))
var1 = name.lower()
var2 = name.replace("ar", "t")