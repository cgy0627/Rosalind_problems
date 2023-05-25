def find_kmers(seq, k):
    return sorted([seq[i:i+k] for i in range(len(seq)-k+1)], reverse=True)

def find_shared_motif(dnas):
    dnas = sorted(dnas, key=lambda x: len(x))
    motifs = [dnas[0]]
    k = len(dnas[0])

    while motifs:
        motif = motifs.pop()
        included = 1
        for dna in dnas:
            if motif not in dna:
                included = 0
                break
        
        if included:
            break
        
        if not motifs and k-1 > 0:
            k -= 1
            motifs = find_kmers(dnas[0], k)

    return motif

dnas = []
with open("rosalind_lcsm.txt", "r") as f:
    lines = f.readlines()
    seq = ''
    for line in lines:
        if line.startswith(">"):
            if seq:
                dnas.append(seq)
            seq = ''
        else:
            seq += line.strip()
            
print(find_shared_motif(dnas))
