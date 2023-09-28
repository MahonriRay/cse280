# Sets  
$\overline{A}  \cup \overline{B}$  $\equiv \overline{A \cap B}$  
Everything except what intersects  

## Set Laws  
Identity:  
A $\cup$  = A  
          A $\cap$  = A  

Domination:  
A $\cap$ 0 = 0  
A $\cup$ Univ = Univ  

Complement:  
A $\cap  \overline{ A}$ = 0  
A $\cup \overline{A}$ = Univ  

De Morgan:  
$\overline{A \cap B}$ = $\overline{A} \cup \overline{B}$  





## Power Set  
P(A) = set of all subsets of A  
A = {1,2,3}  
P(A) = {{1},{2},{3},{1,2},{2,3},{1,3},0,{1,2,3}}  
|P(A)| = 8 = $2^{|A|}$   

A = {1,2,3}  
B = {4,5,6,7}  

AxB  
||4|5|6|7|  
|:-:|:-:|:-:|:-:|:-:|  
|1|(1,4)|(1,5)|(1,6)|(1,7)|  
|2|(2,4)|(2,5)|(2,6)|(2,7)|  
|3|(3,4)|(3,5)|(3,6)|(3,7)|


AxB = {(x,y)|x $\in$ A, y $\in$ B}  
AxB = {(x,y)|x $\in$ B, y $\in$ A}  

AxA = $A^{2}$  

## Pairwise Disjoint Sets  
A = {x|x $\in \mathbb{Z}$, x is a multiple of 3}  
B = {x|x $\in \mathbb{Z}$, x is odd}  
C = {3,7,11}  
D = {6,8,10}  

Disjointed: X $\cap$ Y = 0  
ALL PAIRS must be disjointed in order to be Pairwise Disjointed  

## Partitions  
Partition set A into $P_{i}$  
$P_{i}$ is a partition ;ff  
1. $P_{i}$ $\le$ A  $P_{i}$ = A  --Powerset
2. $P_{i}$ $\neq$ 0  --Remove
3. All $P_{i}$ are pairwise disjoint  --Remove
4. $P_{1} \cup P_{2} \cup P_{3} .... \cup P_{i}$ = A  --Verify  

A = {a,b}  
$P_{1}$ : {a},{b}  
$P_{2}$ : {a,b}  

A = {1,2,3,4}  
$P_{1}$ = {1,2,3,4}  
$P_{2}$ = {1}, {2}, {3}, {4}  
....  
$P_{11}$ = {1},{3}, {2,4}  

S = {x|x $\in \mathbb{Z}$, -5 $\le$ x $\le$ 5}  
$P_{1}$ = {5}, {-5}, {-4,-3,-2,-1,0,1,2,3,4} <- Equivalence Class  

{Expression|Loop, Condition}

