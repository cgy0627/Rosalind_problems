from itertools import product

res = open('result.txt', 'w')
with open('rosalind_lexf.txt', 'r') as f:
    lines = f.readlines()
    lst = list(lines[0].strip().split(' '))
    n = int(lines[1].strip())

    combos = product(lst, repeat=n)
    for combo in combos:
        print(''.join(combo), file=res)

res.close()

