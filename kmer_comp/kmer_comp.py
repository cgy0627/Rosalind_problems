from itertools import product

def kmer_count(s, k):
    kmers = {}
    for i in range(len(s)-k+1):
        kmer = s[i:i+k]
        if kmer in kmers:
            kmers[kmer] += 1
        else:
            kmers[kmer] = 1
    
    return kmers

with open('rosalind_kmer.txt', 'r') as f:
    seq = ''
    for line in f.readlines():
        if not line.startswith(">"):
            seq += line.strip()
    
    kmers = list(map(lambda x: ''.join(x), product(['A', 'C', 'G', 'T'], repeat=4)))
    
    count = kmer_count(seq, 4)
    for kmer in kmers:
        if kmer in count:
            print(count[kmer], end=' ')
        else:
            print(0, end=' ')
