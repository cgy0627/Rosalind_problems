def fibonacci(n):
    a,b = 0,1

    for i in range(2, n+1):
        a,b = b,a+b
    
    print(b)

fibonacci(20)
