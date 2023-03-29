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

### [Lecture. 5] Tuples, Lists, Aliasing, Mutability, Cloning  

Tuple - immutable, inside anything  
List = indices and ordering, "Mutable!"(can change value), iterable  
<-> string(join method) // can cast type, vice versa  

list method  
- append(add) / + is combine between two lists  
- remove; specific index / pop; end of list  
- join  
- sort(mutates the list, returns nothing), sorted(does not mutate, return), reverse  
cf) '.'= operation,  
<br/>

- objects; lists assign same object,  
list of list of ... ; can have nested, side effects still possible after mutation  
avoid mutating a list as u are iterating over it  
[list]  
- **mutable**(e.g. copy)  
- is an **object** in **memory**  
- variable name points to object  
** **Mutation, Aliasing, Cloning ****


---

### [Lecture. 6] Recursion and Dictionaries  

- Recursion) **divide** and conquer / **decrease** and conquer  
- Dictionaries) mutable object type  

- Recursion  
  - Algorithmically(iterative, state variavles) & Semantically(function calls itself)
  - cans solve directly and simple = computation
  - own scope & environment, using the same variable names but **different objects in separate scopes**, flow of ctrl passes **back to previous scope**
  - but avoid infinite condition, bounded, needed base case
  - its can be very straightforward, just unwind it simple and the code follows exactly that.  

```python
# Towers of Hanoi

def printMove(fr, to):
  print(‘move from’ + str(fr) + ‘to’ + str(to))

def Towers(n, fr, to, spare):
    if n == 1:
        printMove(fr, to)
else:
    Towers(n-1, fr, spare, to)
    Towers(1, fr, to, spare)
    Towers(n-1, spare, to, fr)
```

e.g.) Fibonacci numbers  
e.g.) Palindrome  

- Dictionaries; a better and cleaner way(than list or etc.)
  - store pairs of data(key & value)
  - add, test(search), delete, get an iterable like a tuple of all keys/vals
  - values(immutable and mutable, duplicates) vs keys(unique, immutable, no order)
  - dic can be used like dp for fibonacci(like memoization)  

---

### [Lecture. 7] Testing, Debugging, Exceptions, and Assertions

- defensive programming; Testing/Validation & debugging  
  - specifications for functions, modularize,  

- * Unit testing - testing each function one by one.  
- Regression - catch reintroduced  
- Integration - overall program  

- black box testing -  
- glass box testing – path-complete / drawback; branchesm, for loops, while loops
- Debugging – built in / Tutor / print statement / systematic in my hunt, use brain

![Tips](https://user-images.githubusercontent.com/94775103/223929475-395f0646-a61c-4092-b68d-d594b9208fb9.png)

- Error types
  - SyntaxError / NameError / AttributeError / TypeError / ValueError / IOError
  - Python code can provide **handlers** for exceptions => try:, except:, finally:

- Assertion
  - want to be sure that assumptions expected, is an example of good defensive programming
  - use for execution halts / check inputs&outputs; types, invariants, constraints, violations

---

### [Lecture. 8] Object Oriented Programming(OOP)

- Objects
  - type, data representation, a set of procedures for interaction with the object
  - data abstraction; an internal representation(private) / an interface

- Advantages of OOPs
  - bundle data into **packages**
  - divide-and-conquer
  - **classes** make it easy to **reuse** code
  - **creating a class**(define, **inherits,** data and procedures that **belong** to – data attributes & methods) and **using an instance**
  - special operators(double underscore; e.g. __add__, dot notation(‘.’ operator) to access data)

---


