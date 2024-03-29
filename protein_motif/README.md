# Finding a Protein Motif

[문제 링크](https://rosalind.info/problems/mprt/)

### 문제 설명

<p>To allow for the presence of its varying forms, a protein motif is represented by a shorthand as follows: [XY] means "either X or Y" and {X} means "any amino acid except X." For example, the N-glycosylation motif is written as N{P}[ST]{P}.</p>
<p>You can see the complete description and features of a particular protein by its access ID "uniprot_id" in the UniProt database, by inserting the ID number into http://www.uniprot.org/uniprot/uniprot_id</p>
<p>Alternatively, you can obtain a protein sequence in FASTA format by following http://www.uniprot.org/uniprot/uniprot_id.fasta</p>
<p>For example, the data for protein B5ZC00 can be found at http://www.uniprot.org/uniprot/B5ZC00.</p>
<p>Given: At most 15 UniProt Protein Database access IDs.</p>
<p>Return: For each protein possessing the N-glycosylation motif, output its given access ID followed by a list of locations in the protein string where the motif can be found.</p>

### 입출력 예
<table class="table">
 <thead>
  <tr>
   <th>s</th>
   <th>return</th>
  </tr>
 </thead>
 <tbody>
  <tr>
   <td>
    A2Z669</br>B5ZC00</br>P07204_TRBM_HUMAN</br>P20840_SAG1_YEAST
   </td>
   <td>B5ZC00</br>85 118 142 306 395</br>P07204_TRBM_HUMAN</br>47 115 116 382 409</br>P20840_SAG1_YEAST</br>79 109 135 248 306 348 364 402 485 501 614
   </td>
  </tr>
 </tbody>
</table>
