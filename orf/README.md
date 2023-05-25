# Open Reading Frames

[문제 링크](https://rosalind.info/problems/orf/)

### 문제 설명

<p>Either strand of a DNA double helix can serve as the coding strand for RNA transcription. Hence, a given DNA string implies six total reading frames, or ways in which the same region of DNA can be translated into amino acids: three reading frames result from reading the string itself, whereas three more result from reading its reverse complement.</p>
<p>An open reading frame (ORF) is one which starts from the start codon and ends by stop codon, without any other stop codons in between. Thus, a candidate protein string is derived by translating an open reading frame into amino acids until a stop codon is reached.</p>
<p>Given: A DNA string s of length at most 1 kbp in FASTA format.</p>
<p>Return: Every distinct candidate protein string that can be translated from ORFs of s. Strings can be returned in any order.</p>

### 입출력 예
<table class="table">
 <thead>
  <tr>
   <th>input</th>
   <th>return</th>
  </tr>
 </thead>
 <tbody>
  <tr>
   <td>>Rosalind_99</br>AGCCATGTAGCTAACTCAGGTTACATGGGGATGACCCCGCGACTTGGATTAGAGTCTCTTTTGGAATAAGCCTGAATGATCCGAGTAGCATCTCAG</td>
   <td>MLLGSFRLIPKETLIQVAGSSPCNLS</br>M</br>MGMTPRLGLESLLE</br>MTPRLGLESLLE</td>
  </tr>
 </tbody>
</table>
