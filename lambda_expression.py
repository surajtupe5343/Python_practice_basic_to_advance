def last_ch(a):
    return a[-1]
print(last_ch('tupe'))

last_char = lambda a : a[-1]
print(last_char('suraj'))

def func(s):
    if len(s)>5:
        return True
    return False

func1 = lambda s : True if  len(s)>5 else False
func1 = lambda s : len(s)>5 #---> true/false can be write like this.
print(func1('suddhd'))