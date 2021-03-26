# PairwiseLocalAlignment

Bioinformatics course first assignment at Amirkabir University of Technology.

In this assignment, pairwise local alignment is addressed and to do so, "Dynamic Programming" method is used.

Gap penalty is considered as 5 and score of match/miss-match is driven using PAM250.

Input of this program is two strings with capital letters which each one comes in a new line and represents a protein.

Output is consist of 3 lines.<br>
* in the first line, alignment score will be printed.
* in the second and third line, local alignments including - on behalf of the gap will be printed.

Regrading traceback, when scores are equal, following order is considered.
1. returning from left
2. returning from top
3. returning from match/miss-match state

* And the result will be returned as soon as it gets a 0 in a cell.

some examples:
1. <b>input:</b><br>MEANLYPRTEINSTRING<br>PLEASANTLYEINSTEIN<br><br>
<b>output:</b><br>23<br>LYPRTEINSTRIN<br>LY---EINSTEIN
   

2. <b>input:</b><br>HEAGAWGHE<br>PAWHEA<br><br>
<b>output:</b><br>24<br>AWGHE<br>AW-HE
