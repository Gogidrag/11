from itertools import product
k=0
for i in product('НАСТЯ', repeat=6):
    if i.count('А')>1:
        continue
    if i.count('Я')>1:
        continue
    k+=1
print(k)