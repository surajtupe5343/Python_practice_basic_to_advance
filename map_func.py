from typing import Tuple


names = ['abc', 'abcd', 'abcde']
l_1 = (map(len,names))#---> we can use list tuple set functions to convert it into list or tuple 
print(l_1)
for i in l_1:
    print(i)

for j in l_1:
    print(j)#----> it will not print because map object can print loop only once. but when we convert it into list or tuple then we can print loop 1000times 