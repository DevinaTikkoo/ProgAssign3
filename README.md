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
The input file will always...

## Running Repository 
Once the repository is cloned, run the program from the root directory with the following command...

python src/main.py tests/<input_file>

If successful, the output will be two printed lines. The first line is the maximum value or arr[i][j] of a common subsequence of the inputted strings. The next line contains one otimal subsequence that produces the previous value.

Additionally, the input files within the tests directory are used for the examples in Question 1. To measure their runtimes use the following command...

python src/measure.py

The measure function automatically finds the 10 input files from tests/question1 and reads their input. Then to graph the run-times run..

python src/generate.py 



## Question 1
