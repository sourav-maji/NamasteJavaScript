import re

text = '''The gross cost of operating lease vehicles in FY2021 Q1 was $4.85 billion.
In previous quarter i.e. FY2020 Q4 it was $3 billion. '''


pattern = "FY\d{4}\s\w[1-4]"

res=re.findall(pattern,text)
print(res)

#Ignoring the case
res1=re.findall(pattern.lower(),text,re.IGNORECASE)
print(res1)