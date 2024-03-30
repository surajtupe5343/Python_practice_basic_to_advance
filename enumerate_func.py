names = ['abc', 'def', 'geh', 'suraj']
# pos = 0
# for name in names:
#     print(f"{pos}-->{name}")
#     pos += 1

# -----------------SOLUTION USING enumerate FUNCTION--------------

for pos, name in enumerate(names):
    print(f"{pos}-->{name}")

# ------------------------Second Solution-------------------

# print(names.index('suraj'))

# -----------------SOLUTION USING enumerate FUNCTION--------------

def find_pos(l, target):
    for pos, name in enumerate(l):
        if name == target:
            return f"{target} is at {pos} Position" 
    return 'not in list'

print(find_pos(names,'abc'))