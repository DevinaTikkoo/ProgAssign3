# ProgAssign3
Devina Tikkoo, 61945909

## Project Description 
This program utilizes dynamic programming to find the optimal subsequence of strings a and b such that it maximizes the sum of the value of the characters within the subsequence. 

## Repository Structure 
```text
ProgAssign3
├── data
│ ├── example1.in
│ ├── example2.in
│ └── example3.in
├── src
│ └── generate.py
│ └── generate.py
│ └── generate.py
│
├── tests
│ ├── test1.in
│ └── test2.in
│ ├── test3.in
│ └── test4.in
│ ├── test5.in
│ └── test6.in
│ ├── test7.in
│ └── test8.in
│ ├── test9.in
│ └── test10.in
│
└── README.md
```

## Initial Assumptions
The input file will always follow the provided format with the first line being a non-negative integer K. Additionally, all characters listed are unique and strings can be of different length. 

## Running Repository 
Once the repository is cloned, run compute the Val(c) from the root directory with the following command...

python src/main.py tests/<input_file>

If successful, the output will be two printed lines. The first line is the maximum value or arr[i][j] of a common subsequence of the inputted strings. The next line contains one optimal subsequence that produces the previous value.

Additionally, there are input files within the tests directory are used for the examples in Question 1. To measure their runtimes use the following command...

python src/measure.py

The measure function automatically finds the 10 input files from tests/question1 and reads their input. Then to graph the run-times run..

python src/generate.py 

## Question 1

![Runtime Graph](runtimes\graph.png)

The above graph shows the runtime of 10 input files from tests/question 1 with increasing sizes from 25 to 230. Initial overhead shows a spike within the first few ms, but overall there's an increase in runtime as input string size increases. Specifically, one that matches O(m*n).

## Question 2

To compute the recurrence relation, define OPT(i, j) as the maximum value of the common subsequence between the first i characters of A (a1, a2,... an) and j of B (b1, b2,... bn). The base cases are defined as when no common subsequence exists or when either input string has length 0: OPT(i, 0) = 0 or OPT(0, j) = 0. 

Additionally, we have 2 other cases: character match or mismatch. If there is a match, where A[i] = B[i], then check the character's value and if so add it and recurse on the previous value or just skip the current value v(A[i]). A mismatch would mean the characters do not equal to each other and we must recurse on the character with the larger weight (skip the smaller weight)

As such the recurrence relation as 3 cases and looks as follows...

OPT[i][j] = 0, if i = 0 or j = 0
OPT[i][j] = max(OPT(i-1,j), OPT(i, j-1), OPT(i-1,j-1)+v(A[i])), if A[i] = B[i]
OPT[i][j] = max(OPT(i-1,j), OPT(i,j-1)), if A[i] != B[i]

## Question 3

The pseudocode would utilize the recurrence relation from question 2. Regarding data structures, it will need a 2D array of length nxm that represent the lengths of strings A and B repesctively. 

def HVLCS(A, B, vals): 
    m = length(B)
    n = length(A)

    array = [] 
    #BASE CASE: Fill with 0s
    for i = 0 to n: 
        OPT[i][0] = 0
    for j = 0 to m: 
        OPT[0][j] = 0  
    
