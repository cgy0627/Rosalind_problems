codon = {}
with open("aa_codon.txt", "r") as f:
    for line in f.readlines():
        aa = line.split()
        for i in range(0, len(aa), 2):
            if aa[i+1] in codon:
                codon[aa[i+1]] += 1
            else:
                codon[aa[i+1]] = 1

def rev_translation(protein):
    ans = 3
    for aa in protein:
        ans *= codon[aa]
    
    return ans

with open('rosalind_mrna.txt', 'r') as f:
    print(rev_translation(f.readline().strip()) % 1000000)

