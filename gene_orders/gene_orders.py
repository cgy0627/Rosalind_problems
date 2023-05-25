def factorial(n):
    ans = 1
    while n > 1:
        ans *= n
        n -= 1
    
    return ans

def perm(nums, k=0):
    if k == len(nums):
      print(' '.join(map(str, nums)), file=res)
    else:
        for i in range(k, len(nums)):
            nums[k], nums[i] = nums[i] ,nums[k]
            perm(nums, k+1)
            nums[k], nums[i] = nums[i], nums[k]

def gene_orders(n):
    total = factorial(n)
    print(total, file=res)
    nums = list(range(1, n+1))
    perm(nums)

res = open('result.txt', 'w')
with open('rosalind_perm.txt', 'r') as f:
    n = int(f.readline().strip())
    gene_orders(n)
res.close()

