seq1, seq2 = '', ''
with open("rosalind_hamm.txt", "r") as file:
    seq1 = file.readline().strip()
    seq2 = file.readline().strip()

print(sum(seq1[i] != seq2[i] for i in range(len(seq1))))
