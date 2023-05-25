def complement_dna(s):
    return s.upper().replace('A', 't').replace('T', 'a').replace('G', 'c').replace('C', 'g').upper()

def restriction_site(s):
    comp_s = complement_dna(s)

    for k in range(4,13):
        for i in range(len(s)-k+1):
            if s[i:i+k] == comp_s[i:i+k][::-1]:
                print(i+1, k, file=res)

res = open('result.txt', 'w')
with open('rosalind_revp.txt', 'r') as f:
    s = ''
    for line in f.readlines():
        if not line.startswith('>'):
            s += line.strip()
    
    restriction_site(s)
res.close()
