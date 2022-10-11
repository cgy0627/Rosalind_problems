from Bio import SeqIO
# from Bio.SeqUtils import GC

max_gc = 0
max_gc_id = ""
for record in SeqIO.parse("rosalind_gc.txt", "fasta"):
    id, seq = record.id, record.seq.upper()
    gc_content = (seq.count('G') + seq.count('C')) / len(seq) *100      # GC(seq)
    if gc_content > max_gc:
        max_gc_id = id
        max_gc = gc_content

print(max_gc_id)
print(max_gc)
