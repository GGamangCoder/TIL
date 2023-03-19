# INTRO(웹 페이지 구성요소)  
: HTML(구조 - 레이아웃), + CSS(표현 - 스타일링), + JS(동작 - 인터렉션)  

참조) [MDN](https://developer.mozilla.org/index.html)

<br>

## HTML: Hyper Text Markup Language  
- Hyper Text; 참조(하이퍼링크)를 통해 사용자가 문서 간 접근할 수 있는 텍스트
- Markup Language; 태그 등을 이용하여 문서나 데이터 구조 명시(HTML, Markdown)
> 웹 페이지를 작성/구조화 하기 위한 언어  

**cf) MDN, W3Schools**

### 기본 구조  
- html
	- 문서의 최상위(root) 요소
- head
	- 문서 메타데이터(데이터를 위한 데이터, 속성 정보) 요소
	- 제목, 인코딩, 스타일, 외부 파일 로딩 등.
	- 일반적으로 브라우저에 나타나지 않는 내용(문서 메타데이터 요소)
- body
	- 문서 본문, 실제 화면 구성

<br>

- 요소; 태그(tag)와 내용(content)으로 구성, 중첩(nasted) 가능
- 속성; 각 태그별로 사용할 수 있는 속성이 다름, **공백 없이 & 쌍따옴표("") 사용**
- HTML Global Attribute; 모든 HTML 요소가 공통으로 사용할 수 있는 대표 속성(id, class, style)  

<br>

- 인라인/블록 요소
- 텍스트 요소
	- `<a>` : 다른 url 연결하는 하이퍼링크 생성
	- `<b>, <strong>` : 굵은 글씨, 강조
	- `<i>, <em>` : 기울임
	- `<br>` : 줄 바꿈
	- `<img>` :
	- `<span>` : 의미 없는 인라인 컨테이너
- 그룹 요소
	- `<p>` : 문단
	- `<hr>` : 주제 분리 수평선
	- `<div>` : 의미 없는 블록 레벨 컨테이너
- form
- input & label
	- input 의 초점을 label 로 활성화 가능
	- **input 의 id 속성과 label 의 for 속성을 일치시킨다**
	- input type) text, password, email, number, file / checkbox, radio

<br>

## CSS: Cascading Style Sheets, 스타일 지정하기 위한 언어  
- 요소; 선택자(Selector), 선언(Declaration), 속성(Property), 값(value)
- 정의 방법; 인라인(inline), 내부 참조, 외부참조(link file- css파일)  
<br>
- 선택자 유형  
- 전체 선택자(*), 요소 선택자(tag), 클래스 선택자(.), 아이디 선택자(#) - 일반적으로 1번만 사용(단일 id)  
<br>
- 우선순위(cascading order); 중요도(!important) -> 우선순위(인라인 > id > class, 속성 > 요소)

- 상속(inheritance)
	- 상속 되는 것; text 관련 요소(font, color, ...), opacity(투명도), visibility 등
	- 상속 X; Box model 관련 요소(w, h, m, p, border, ...), position 관련 요소(top, bottom, ...)

- 자식, 자손;   ```.box > p```  / ```.box p``` (꺾새 ' > ' 표시 or 빈칸 ' ')

* [CSS 더 알아보기](./02CSS.md)  

<br>

## JS(JavaScript)  
- to be continued

