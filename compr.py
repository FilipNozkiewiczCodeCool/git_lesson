import random 



# for i in range(10):
#     a.append(random.randint(0,100))

a = [ random.randint(0,100) for i in range(10) ]

l = [1,2,3,4,5,6]

#potegi = []
# for i in l:
#     potegi.append(i**2)
potegi = [ i**2 for i in l ]
print(potegi)