## 마크다운(MarkDown) 문법 사용 메뉴얼

참고(출처): https://www.markdownguide.org/cheat-sheet/
<br/>  

## 마크다운(markdown)
- 텍스트 기반의 가벼운 마크업(markup) 언어  
                    : 태그를 사용하여 문서의 구조를 나타내는 것
- **문서의 구조**와 **내용**을 같이 쉽고 빠르게 적고자 탄생
- 단순한 글자를 어떻게 표현할 지를 정의하는 문법이 정의된 언어

## 마크다운 헤딩
'#' 의 갯수로 가능(h1~h6)  
`# heading1`
# heading1
`## heading2`
## heading2
`### heading3`
### heading3
`#### heading4`
#### heading4
`##### heading5`
##### heading5
`###### heading6`
###### heading6

## 순서 작성
```
1. 첫 번째
    1. tab으로 구분 가능
2. 두 번째
```  
1. 첫 번째  
    1. 1-1
2. 두 번째  
## 순서 작성(2)  
: 순서가 없는 것은 다음과 같이 가능
```
- 순서
* 단계
```
- 순서
* 단계

## 인라인 코드 블럭
```md
tip 1개; `(라인 하나만)`
tip 3개;
' ```py(언어)'
    /내용/
' ``` '
```

하다가 `코드` 작성  
//예시 코드
```py
print("Hello!")
```

## 강조 표시
```
*글자* / _글자_                   - 기울이기
**글자**                          - 강조
~~글자~~                          - 취소선
--- / ===                         - 구분선
```  

*글자*  _글자_  
**글자**  
~~글자~~ 
<br/>

---  

## 링크 삽입  
` [이름](url) `
> [구글](https://google.com)

## 이미지 삽입
* 마크다운 문법  
`![이름](url)    앞에 느낌표 작성, 작업 중인 경로.파일`
<br/>

* HTML 이용  
`<center><img src = "" width="300" height="300"></center>`  
여기서 width 와 height 는 크기(기본 px)를 조절하며 *`<p align="center"><img src url></p>`* 기능으로 중앙 정렬이 가능하다.  
<br/>

<p align="center"><img src='https://user-images.githubusercontent.com/94775103/211955363-0325363f-1e24-4b58-8f5d-65092f81b37c.png' width="300" height="300"></p>



## 추가 참고 사항 - HTML
### 줄 간격 띄우기  
1. 스페이스바(space bar) 두 번!  
2. <'br/'> 작성 후 엔터  

### 띄어쓰기(줄 바꿈 없는 공백)
1. `&nbsp;` 작성

### 인용/들여쓰기
```
'>' 꺾새 표시 후 줄간격(' ') 한 번
```
> 들여쓰기

### 특수기호 부르는 법
" - " : hyphen(하이픈), dash(대시)  
" / " : slash(슬래시)  
" * " : asterisk(별, star)  
" ` " : backtick  
" \ " : backslash  

***
끝
