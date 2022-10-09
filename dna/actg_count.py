def actg_count(dna):
  dna = dna.lower()
  return dna.count('a'), dna.count('c'), dna.count('g'), dna.count('t')

a,c,g,t = actg_count('GTGTCTCTCGAGTGGCCTTTCTCCTATGGTTCTATTCTGTCTAAACACCCAGACCATGTGGGTAGAACACCAGTTCGATTTCGTTAGTCAGAACTTTAGGAACGAGGGTCAAGCGGGTCTTATAATTCTCCAAAATGCGCCTAACGGGACCAAGTCAATTCTGGAACTTATCTAAACATTCGGGGCCCTTGTTAGTTACACCCTTTTACGACCCAGAAGCGCTGGCCCGCGCAATCAAGATAGACAGTCCAGAGAGCTTTGGCACCTGGCGATTACTCGGCTTAGATCAAAAATGTACGGTGTTGATAATCTGAGCCACCTTGCCTATTCTCCCAACCGCGCACAGACACTGAGGAGGGCGACATTCCCGTACCAATGCTTAAGTGTGGTCACAGGCTGATGGTACCACCCTTCTCCATAGGCCCTGATGGGAGAGGTCGCCCGATTCATGGATAAGGAGGTTCCCACGATGGGGGCAGGGGCTTAATGAGTCTTTCCGTTTAGACTCGTAATCCTTCGAGGCAATCGTGCCTTCTATAAACCTCGCCACTCGCATATTGCCCGCCACCCGGTAGGCCGTCTCTACACCCACTGGAGATCGACGGTTTGCTTTGCTAGACGCTAGTGCTTTGGTACGTACTACACAGATATTCTTGGCGGTCACTACGATCCTAGTAGGCACGACACCTCATAATAGAACTTACCACGTGATGAAATTGTAGCCATCTGGTTAGAATATTAGAGGAGACCAGGCTGTCCCCGATAGGCCATCACAGCTCCGCAAGATCACACCTTGCAAACTGTTAGAGGATATACGGGATCGTGTGATTAAATCCGAGATCTTTCCTTGAAAAACAAGGTTGGTTCCAATATCGAACCGTCAAATAAGCTGACACCACCGGGGAACGGGTGCACGAAAAACCTAATGGCTGGGCAATAAGTTGGGTACTGTGTGGGG')
print(a,c,g,t)
