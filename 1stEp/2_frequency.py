str = "Sheena love eating apple and mango. His sister also love eating apple and mango"



new_str = str.replace("apple","")
print(new_str)
print((len(str) - len(new_str))// len("apple"))



d={}
li = str.split()
for i in li:
    if i not in d.keys():
        d[i]=0
    d[i]+=1
print(d)

# from collections import Counter

# print(Counter(str))


dic ={}
new_li = str.split()
for i in new_li:
    if i not in dic.keys():
        dic[i] =0
    dic[i]+=1
print(dic)