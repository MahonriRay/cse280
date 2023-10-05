# CSE 280 Prove 03

(c) BYU-Idaho - It is an honor code violation to post this
file completed or uncompleted in a public file sharing site.

**Instructions**: Answer each question using proper markdown notation as needed.  Use the preview view in Visual Studio Code (or another editor if desired) to see the formatting, tables, and mathematical formula properly rendered.  If you need to write code, then first test your code in a separate file and then copy the code into this document using code fences. 

**Name**: Mahonri Mo Ray

**Section**: MWF 10:15 - 11:15

**Teacher**:Brother Chad MacBeth

## Question 1 (5 points)

Let $E$ be the set of even numbers, and let $P$ be the set of prime numbers.  Find all the values in the set formed by $E \cap P$.

**Answer**:  It would be 2 and only two since 2 is the only prime number that is also even.

## Question 2 (5 points)

Let the following sets be given.  The Universal set for this problem is the set of all students at some univeristy:

* $F$ = the set of all freshmen
* $M$ = the set of all math minors
* $C$ = the set of all CS majors

Translate $(F \cap M) \subseteq C$ into an english sentance.

**Answer**: The intersecting students who are math minors and freshmen taken from all of the CS majors 

## Question 3 (5 points)

For each set described below, list 4 example values that would be in that set.  The first one is done for you.  Remember that $\mathbf{Z}$ represents integers and $\mathbf{Z}^+$ represents positive integers greater than 0.  

|Set|Four Example Values in the Set|
|:-:|:-:|
|$\lbrace x \in \mathbf{Z}^+ \mid x-1 \text{ is a multiple of 7} \rbrace$|{8,15,22,29}|
|$\lbrace x \mid x \text{ is a fruit and its skin is normally eaten} \rbrace$|{apple, strawberry, grape, blueberry}|
|$\lbrace \frac 1 x \mid x \in \mathbf{Z}, x \neq 0 \rbrace$|{$ \frac 1 2, \frac 1 3, \frac 1 4, \frac 1 5$}|
|$\lbrace 2n \mid n \in \mathbf{Z}, n \lt 0 \rbrace$|{-2, -4, -6, -8}|
|$\lbrace s \mid s = 1 + 2 + ... + n \text{ for some } n \in \mathbf{Z}^+ \rbrace$|{1, 3, 6, 10}|

## Question 4 (9 points)

Let $A = \lbrace 0, 2, 3 \rbrace$, $B = \lbrace 2, 3 \rbrace$, and $C = \lbrace 1, 5, 9 \rbrace$, and the universal set $U = \lbrace 0, 1, 2, ...,  9 \rbrace$.  Determine the resulting sets for the following operations.  The first one is done for you,

|Operation|Resulting Set|
|:-:|:-:|
|$A \cap B$|$\lbrace 2, 3 \rbrace$|
|$A \cup B$|$\lbrace 0,2,3 \rbrace$|
|$B \cup A$|$\lbrace 0,2,3 \rbrace$|
|$A \cup C$|$\lbrace 0,1,2,3,5,9 \rbrace$|
|$A - B$|$\lbrace 0 \rbrace$|
|$B - A$|$\lbrace  \rbrace$|
|$\overline{A}$|$\lbrace 1,4,5,6,7,8,9 \rbrace$|
|$\overline{C}$|$\lbrace 0,2,3,4,6,7,8 \rbrace$|
|$A \cap C$|$\lbrace  \rbrace$|
|$A \oplus B$|$\lbrace 0 \rbrace$|

## Question 5 (4 points)

Let $A=\lbrace 0, 2, 3 \rbrace$, $B=\lbrace 2, 3 \rbrace$, and $C=\lbrace 1, 4\rbrace$ and let the universal set $U=\lbrace 0, 1, 2, 3, 4 \rbrace$.  List the element pairs for each of the following cartesian products using these sets.  The first one is done for you.

|Cartesian Product|Answer|
|:-:|:-:|
|$A \times B$|$\lbrace (0,2), (0,3), (2,2), (2,3), (3,2), (3,3) \rbrace$|
|$B \times A$|$\lbrace (2,0),(2,2),(2,3),(3,0),(3,2),(3,3) \rbrace$|
|$A \times B \times C$|$\lbrace (0,2,1), (0,2,4) (0,3,1), (0,3,4) (2,2,1), (2,2,4), (2,3,1), (2,3,4), (3,2,1), (3,2,4), (3,3,1), (3,3,4) \rbrace$|
|$A \times \overline{A}$|$\lbrace (0,1),(0,4),(0,5),(0,6),(0,7),(0,8),(0,9),(2,1),(2,4),(2,5),(2,6)(2,7),(2,8),(2,9),(3,1)(3,4)(3,5),(3,6)(3,7),(3,8),(3,9) \rbrace$|
|$B^2$|$\lbrace (2,2),(2,3),(3,2),(3,3) \rbrace$|

## Question 6 (5 points)

Which pairs (there may one pair or more than one pair) of the following sets are pairwise disjoint:

* $A =$ The set of all even numbers.
* $B =$ The set of all odd numbers.
* $C =$ The set of all non-negative powers of 2.

Hint: Make a list of numbers that are in each of these sets.

**Answer**: A $\cap$ B are pairwise disjoint because a number cannot be both even and odd.  
B $\cap$ C are not pairwise disjoint because all non negative powers of two will always be even except for zero. 0 $\mathbb{^2} = 1, which is odd.$

## Question 7 (5 points)

List all of the partitions  (how many ways can we split according to the rules of partitions) of the set $A = \lbrace a, b, c \rbrace$.

**Answer**:  
||A|  
|:-:|:-:|   
|$P_{1}$|$A_{1} = a,  A_{2} = b, A_{3} = c$|  
|$P_{2}$|$$A_{1} = a, b, A_{2} = c$$|  
|$P_{3}$|$$A_{1} = a, A_{2} = b,c$$|  
|$P_{4}$|$$A_{1} = b, A_{2} = a,c$$|
|$P_{5}$|$$A_{1} = a,b,c$$

## Question 8 (12 points)

In Python, you can create sets using "set comprehensions" (which is similar to "list comprehensions").  We read the following $S = \lbrace P(x) \mid x \in D \land C(x) \rbrace$ in English as "$S$ is the set of all values $P(x)$ such that $x$ is an element of the domain set $D$ and satisifies the condition $C(X)$".  We can translate this into Python code as: `S = {P(x) for x in D if C(x)}`.  The function calls `P(x)` and `C(x)` can be other defined functions, other defined lambda functions, or expressions written directly in the set comprehension.  Additionally, $D$ could be a set defined in a different variable or it could be provided directly in the set comprehension.

Recall the use of the `range(a,b)` function in Python to generate an iterable collections from `a` to `b-1`.

Use the starting code below to create set comprehensions as follows:

|Set ID|Set Builder Notation|
|:-:|:-:|
|Set1|$\lbrace \frac 1 n \mid n \in \lbrace 2, 4, 8, 16 \rbrace \rbrace$|
|Set2|$\lbrace n^2 \mid n \in \lbrace -2, -1, 0, 1, 2 \rbrace \rbrace$|
|Set3|$\lbrace n \mid n \in \mathbf{Z}^+,  n \text{ is a factor of } 24 \rbrace$|
|Set4|$\lbrace n \mid n \in \mathbf{Z}, -10 \le n \le 10, n \text { is odd.} \rbrace$|


```python
Set1 = {1/(2**i) for i in range(1,5)} # Add Set Comprehension Code Here
Set2 = {i**2 for i in range(-2,3)} # Add Set Comprehension Code Here
Set3 = {i for i in range(1,25) if (24%i ==0)} # Add Set Comprehension Code Here
Set4 = {i for i in range(-10,11) if(i%2 != 0)} # Add Set Comprehension Code Here

# Note that sets do not maintain order so it may vary
print(Set1)
print(Set2)
print(Set3)
print(Set4)
```