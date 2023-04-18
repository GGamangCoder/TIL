# Bits, Bytes, and Integers(2)

(일부러 한글을 섞어서 정리)

* Unsigned Addition

두 가지를 더할 때 우리는 bit로써 계산,  
경계에 대해서 overflow가 일어난다. w bits 에 대해 2^(w+1) 되는 경우,  

* Two's Complement Addition - 보수, 제일 앞 비트에 대해

1. `-2^(w-1)` ~ `+2^(w-1)-1` -> raise error  
2. -A + -B => +C -> also, raise error
3. +A + +B => -C -> also, raise error

* TAdd Overflow
    - if sum >= 2^(w-1) or sum < -2^(w-1)


* Multiplication
    - Unsigned Multiplication in C
    - 2w 사이즈의 비트가 되어 overflow, mod에 대한 결과만 나옴

shift 로 계산 진행,  
signed에 대해선 앞에 비트는 그대로 유지.  
ex) 1010 >> 1101 >> 1110

보수 = 뒤집은 후(~) + 1


## 정리
* Addition:
    - unsigned/signed: Normal addition followed by truncate(분할), same operation on bit level
    - unsigned: addition mod 2^w, 
    - signed: modified addition mod 2^w(result in proper range)

* Multiplication:
    - 이하 동문(same as above, S/A)


* in JAVA >>> means logical shift

--- 
49분대 강의