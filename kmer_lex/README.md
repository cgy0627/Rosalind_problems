# Enumerating k-mers Lexicographically

[문제 링크](https://rosalind.info/problems/lexf/)

### 문제 설명

<p>Assume that an alphabet A has a predetermined order; that is, we write the alphabet as a permutation A=(a1,a2,…,ak), where a1 < a2 < ⋯ < ak. For instance, the English alphabet is organized as (A,B,…,Z).</p>
<p>Given two strings s and t having the same length n, we say that s precedes t in the lexicographic order (and write s < Lex t) if the first symbol s[j] that doesn't match t[j] satisfies sj < tj in A.<\p>
<p>Given: A collection of at most 10 symbols defining an ordered alphabet, and a positive integer n (n≤10).</p>
<p>Return: All strings of length n that can be formed from the alphabet, ordered lexicographically (use the standard order of symbols in the English alphabet).</p>

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
   <td>A C G T</br>2</td>
   <td>AA</br>AC</br>AG</br>AT</br>CA</br>CC</br>CG</br>CT</br>GA</br>GC</br>GG</br>GT</br>TA</br>TC</br>G
</br>TT</td>
  </tr>
 </tbody>
</table>
