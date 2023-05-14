## RNA Translation

# Doesn't consider RNA having three different frames

codon = {}
with open("aa_codon.txt", "r") as f:
    for line in f.readlines():
        aa = line.split()
        for i in range(0, len(aa), 2):
            codon[aa[i]] = aa[i+1]

def translation(rna):
    protein = ''
    for i in range(0, len(rna), 3):
        protein += codon[rna[i:i+3]]
    
    return protein.replace('Stop', '')
