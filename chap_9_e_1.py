#------------Normal Solution----------------

s1 = ['abc', 'def', 'ghi']
s2 = []
for i in s1:
    s2.append(i[::-1])
print(s2)

#---------------Solution using List Comprehention-----------------

s3 = [i[::-1] for i in s1]
print(s3)

#----------------List comprehention with function-------------

def revrese_strings(l):
    return[i[::-1] for i in l]
 
print(revrese_strings(['abc', 'def', 'ghi']))