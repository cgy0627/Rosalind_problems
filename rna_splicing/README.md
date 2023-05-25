# RNA Splicing

[문제 링크](https://rosalind.info/problems/splc/)

### 문제 설명

<p>After identifying the exons and introns of an RNA string, we only need to delete the introns and concatenate the exons to form a new string ready for translation.</p>
<p>Given: A DNA string s (of length at most 1 kbp) and a collection of substrings of s acting as introns. All strings are given in FASTA format.</p>
<p>Return: A protein string resulting from transcribing and translating the exons of s. (Note: Only one solution will exist for the dataset provided.)</p>

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
   <td>>Rosalind_10</br>ATGGTCTACATAGCTGACAAACAGCACGTAGCAATCGGTCGAATCTCGAGAGGCATATGGTCACATGATCGGTCGAGCGTGTTTCAAAGTTTGCGCCTAG</br>>Rosalind_12</br>ATCGGTCGAA</br>>Rosalind_15</br>ATCGGTCGAGCGTGT</td>
   <td>MVYIADKQHVASREAYGHMFKVCA</td>
  </tr>
 </tbody>
</table>
