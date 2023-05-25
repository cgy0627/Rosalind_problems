def dna_motif(seq, motif):
    ans = []
    for i in range(len(seq)-len(motif)+1):
        if seq[i:i+len(motif)] == motif:
            ans.append(str(i+1))
    
    return ' '.join(ans)

with open('rosalind_subs.txt', 'r') as f:
    lines = f.readlines()

    print(dna_motif(lines[0].strip(), lines[1].strip()))
