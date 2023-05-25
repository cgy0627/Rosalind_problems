def tt_ratio(s1, s2):
    pp = {'A':'purine', 'G':'purine', 'C':'pyrimidine', 'T':'pyrimidine'}
    transitions, transversions = 0, 0

    for i in range(len(s1)):
        if s1[i] != s2[i]:
            if pp[s1[i]] == pp[s2[i]]:
                transitions += 1
            else:
                transversions += 1
    
    return transitions/transversions

with open('rosalind_tran.txt', 'r') as f:
    seq = ''
    seqs = []
    for line in f.readlines():
        if line.startswith(">"):
            if seq:
                seqs.append(seq)
            seq = ''
        else:
            seq += line.strip()
    if seq:
        seqs.append(seq)
    
    print(tt_ratio(seqs[0], seqs[1]))
