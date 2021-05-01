def func1(n):

    if n <= 1:
        return n
    else:
        return(func1(n-1) + func1(n-2))



for i in range(0,10):
        print(func1(i))