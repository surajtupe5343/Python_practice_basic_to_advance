def all_powers(num1, *args):
    if args:
        return [i**num1 for i in args]
    else:
        return "hey you did't pass any args."

nums = [1, 2, 3, 4]
print(all_powers(3, *nums))  #--> 3 gives cube, if I type 2 then it will give Square.