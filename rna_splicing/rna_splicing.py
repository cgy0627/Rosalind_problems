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

with open("rosalind_splc.txt") as f:
    seqs = []
    seq = ''
    for line in f.readlines():
        if line.startswith('>'):
            if seq:
                seqs.append(seq)
            seq = ''
        else:
            seq += line.strip()
    if seq:
        seqs.append(seq)

    dna = seqs[0]
    for i in range(1, len(seqs)):
        dna = ''.join(dna.split(seqs[i]))
    
    rna = dna.upper().replace('T', 'U')
    print(translation(rna))
