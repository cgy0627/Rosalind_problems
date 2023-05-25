# Finding a Shared Motif

[문제 링크](https://rosalind.info/problems/lcsm/)

### 문제 설명

<p>A common substring of a collection of strings is a substring of every member of the collection. We say that a common substring is a longest common substring if there does not exist a longer common substring. For example, "CG" is a common substring of "ACGTACGT" and "AACCGTATA", but it is not as long as possible; in this case, "CGTA" is a longest common substring of "ACGTACGT" and "AACCGTATA".</p>
<p>Note that the longest common substring is not necessarily unique; for a simple example, "AA" and "CC" are both longest common substrings of "AACC" and "CCAA".</p>
<p>Given: A collection of k (k≤100) DNA strings of length at most 1 kbp each in FASTA format.</p>
<p>Return: A longest common substring of the collection. (If multiple solutions exist, you may return any single solution.)</p>

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
   <td>>Rosalind_1</br>GATTACA</br>>Rosalind_2</br>TAGACCA</br>>Rosalind_3</br>ATACA</td>
   <td>AC</td>
  </tr>
 </tbody>
</table>
