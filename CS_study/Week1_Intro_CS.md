# Introduction to Computer Science  
출처) https://ocw.mit.edu/courses/6-0001-introduction-to-computer-science-and-programming-in-python-fall-2016/  

<br/>

### [Lecture. 1] What is computation?

Python = object, typesyntax & type; int, float, boolean, ... value and naming = assign memory in value and reuse equal(=) doesn't mean same, 
it is assign memory in valuecan re-bind variable name using new assignment statements+ previous value may stil stored in memory but lost the handle for it
 * Topics – data structures / iterations and recursion / abstraction / organize and modularize / algorithms / complexity
 * sequence of simple steps -> flow of controls -> when to stop(determining)
 * fixed & stored program
 * ALU) Memory – Control unit <-> ALU

---

### [Lecture. 2] Branching and Iteration

* Strings – concatenate, * (repeat)output keyword = print
input – whatever users types in something and hits enter
- default cast is string comparisons below evaluate to a Boolean
  // vice versa = opposite → lexicographically(사전상); following alphabetabout Algorithm or Problem Solving;
* these sort of decisions are created by you as a programmer, and the computer just has to make the decision and choose a path
* if, else, and else; True or False of condition  
<br/>

* **conditionals and branching(조건 과 분기)**  
while loop; repeat until condition is Flase   
for loops; short cut wit for loopsfor <variable> in range(<some_num>):   
  <expression> ...   
  // parentheses; 괄호   
  range(start, stop, steps)   
  break STATEMENT    

---

### [Lecture. 3]
- string manipulation  
- guess and check algorithm  
- approximate solutions  
- bisection method  

Strings – function(len, indexing(start at 0),  
** can allow indexing but it is “immutable” so that cannot be modified  
    
Bisection Search – higher or lower  
```
N/(2^k) = 1  
N = 2^k  
∴ K = logN  
```

---

### [Lecture. 4] Decomposition, Abstractions, Functions

* Abstractions: we don't know how it works it but how the components work together
* Decompositions: creating structure in code, sort of mini proj
* Functions: maker & user
  - call, scope(LEGB), parameter, name, environment
  - use for multiple times to do

---
