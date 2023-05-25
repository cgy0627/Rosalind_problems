# Locating Restriction Sites

[문제 링크](https://rosalind.info/problems/revp/)

### 문제 설명

<p>A DNA string is a reverse palindrome if it is equal to its reverse complement. For instance, GCATGC is a reverse palindrome because its reverse complement is GCATGC. See Figure 2.</p>
<p>Given: A DNA string of length at most 1 kbp in FASTA format.</p>
<p>Return: The position and length of every reverse palindrome in the string having length between 4 and 12. You may return these pairs in any order.</p>

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
   <td>>Rosalind_24</br>TCAATGCATGCGGGTCTATATGCAT</td>
   <td>4 6</br>5 4</br>6 6</br>7 4</br>17 4</br>18 4</br>20 6</br>21 4</td>
  </tr>
 </tbody>
</table>
