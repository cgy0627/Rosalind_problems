def factorial(n):
    ans = 1
    while n > 1:
        ans *= n
        n -= 1
    
    return ans

with open('rosalind_pper.txt', 'r') as f:
    n, k = map(int, f.readlines()[0].strip().split(' '))

    print(int(factorial(n) / factorial(n-k) % 1000000))
