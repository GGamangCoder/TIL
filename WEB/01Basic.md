# 웹 페이지 구성요소  
: HTML(구조 - 레이아웃), + CSS(표현 - 스타일링), + JS(동작 - 인터렉션)
## HTML: Hyper Text Markup Language  
- Hyper Text; 참조(하이퍼링크)를 통해 사용자가 문서 간 즉시 접근할 수 있는 텍스트
- Markup Language; 태그,  ex) ```<h1> </h1>```
> 웹 페이지를 작성/구조화 하기 위한 언어  

**cf) MDN, W3Schools**

- html; 문서의 최상위(root) 요소
- head; 문서 제목, 인코딩, 스타일, 외부 파일 로딩 등. 일반적으로 브라우저에 나타나지 않는 내용(문서 메타데이터 요소)
  ex) <title> <link> <style>
- body; 문서 본문, 실제 화면 구성

- 요소; 여는/시작 태그 - 내용(contents) - 닫는/종료 태그, 중첩 가능, 태그 쌍 잘 확인
- 속성; 각 태그별로 사용할 수 있는 속성이 다름, 공백 없이 & 쌍따옴표("") 사용
  
cf) 주석; ```<!-- 내용 -->```

- form, input, label(선택할 수 있는 영역 늘어남)
- input & label 상호 연관; input 에는 id 속성, label에는 for 속성을 활용, **일치**시켜야 함!!!



## CSS: Cascading Style Sheets, 스타일 지정하기 위한 언어  
- 선택자(Selector)
- 선언(Declaration)
- 속성(Property)
- 값(value)
  
- 전체 선택자(*), 요소 선택자(tag), 클래스 선택자(.), 아이디 선택자(#)  
  
* ul, li  

- 중요도(!important) **** 제일 먼저,
- 우선순위(중요도 > 인라인 - id - class, 속성 - 요소)

- 상속: **속성 중에 상속이 되는 것이 있고 되지 않는 것들이 있다!!**
- 자식, 자손;   ```.box > p```  / ```.box p``` (꺾새 ' > ' 표시 or 빈칸 ' ')


## JS(JavaScript)  


