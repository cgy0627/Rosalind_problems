from urllib.request import urlopen
import re

with open("rosalind_mprt.txt", "r") as f:
    ids = f.readlines()

# N-glycosylation motif = N{P}[ST]{P}
for id in ids:
    id = id.strip()
    uniprot_id = id.split('_')[0]
    url = f"http://www.uniprot.org/uniprot/{uniprot_id}.fasta"
    response = urlopen(url)
    seq = ''.join(map(lambda x: x.decode('utf-8', 'ignore').replace('\n', ''), response.readlines()[1:]))
    
    res = re.search('N[^P][ST][^P]', seq)
    matches = [0]
    while res:
        start = matches[-1] + res.span()[0] + 1
        matches.append(start)
        # print(start)
        res = re.search('N[^P][ST][^P]', seq[start:])
    
    if len(matches) > 1:
        print(id)
        print(' '.join(map(str, matches[1:])))
