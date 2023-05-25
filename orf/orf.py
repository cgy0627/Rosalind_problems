def rev_complement_mrna(s):
    return s[::-1].upper().replace('A', 'u').replace('U', 'a').replace('G', 'c').replace('C', 'g').upper()

codon = {}
with open("aa_codon.txt", "r") as f:
    for line in f.readlines():
        aa = line.split()
        for i in range(0, len(aa), 2):
            codon[aa[i]] = aa[i+1]

def six_frame_translation(rna):
    rev_rna = rev_complement_mrna(rna)
    proteins = set()

    def three_frame_translation(rna):
        for i in [0,1,2]:
            protein = ''
            for j in range(i, len(rna)-3, 3):
                aa = rna[j:j+3]
                if protein:
                    if codon[aa] == 'Stop':
                        proteins.add(protein)
                        protein = ''
                    else:
                        protein += codon[aa]
                    
                elif protein == '' and aa == 'AUG':
                    protein += codon[aa]
    
    three_frame_translation(rna)
    three_frame_translation(rev_rna)
    
    frags = set()
    for protein in proteins:
        temp = protein.split('M')
        if len(temp) > 2:
            for i in range(2, len(temp)):
                frags.add('M' + ''.join(temp[i:]))

    return proteins | frags

with open('rosalind_orf.txt', 'r') as f:
    seq = ''
    for line in f.readlines():
        if not line.startswith(">"):
            seq += line.strip()

    rna = seq.upper().replace('T', 'U')

    proteins = six_frame_translation(rna)
    for protein in proteins:
        print(protein)
