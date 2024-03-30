def fibonacci_seq(n):
    a = 0 
    b = 1
    if n == 0:
        print(a)
    elif n == 1:
        print(a,b, end = " ")    
    else:
        print(a,b, end = " ")
        for i in range(n-2):
            c = a + b
            a = b
            b = c
            print(b , end=" ")

fibonacci_seq(30)
