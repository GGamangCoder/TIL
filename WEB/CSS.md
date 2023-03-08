# CSS(styling)  
<br/>

## CSS Box Model  
- CSS 원칙1
- from **left&up** to right&down(Normal Flow)
- one box contains(content, padding, border, margin)
  - Content; 실제 내부 내용
  - Padding; 테두리 안쪽 내부 여백 요소에 적용된 배경색, 이미지 포함
  - Border; 테두리 영역
  - Margin; 테두리 바깥 외부 여백
  - 순서 - 상/우-좌/하 (+, %, ccw), shorthand 존재

<br/>

### 크롬 개발자 도구  
- emmet; 자동 완성 기능
  - ```! + tab(enter)```; html 기본 뼈대 자동완성
  - ```.class-name``` => ```<div class="class-name"></div>```
  - cf) css 환경 내에서도 가능함!

- lorem (ipsum); 라틴어, 아무 의미 없는 공간 차지용 +(단어 수) / *(단락 수)  

<br/>

## CSS Display  
- CSS 원칙2
- 인라인(content 요소만 차지)/블록 요소(한 줄 전체 차지)
-  \\-> span  

- display: block
  - 줄 바꿈이 일어나는 요소
  - 화면 크기 전체 가로 폭 차지
  - 블록 요소 안 인라인 레벨 요소 들어갈 수 있음
  - ex) div / ul, ol, li / p / hr / form 등  

- display: inline
  - 줄 바꿈 일어나지 않는 행의 일부 요소
  - content 영역만 차지
  - width, height, margin-top, margin-bottom 을 지정할 수 없다.
  - ex) span / a / img / input, label / b, em, i, strong 등  

- display: inline-block
  - block 과 inline 레벨 요소 특징 모두 가짐  

- display: none
  - 해당 요소를 화면에 표시x, 공간도 부여되지 않음
  - ```visibility: hidden``` 은 공간은 차지하나 화면에 표시만 하지 않음

<br/>

## CSS position  
- 문서 상에서 요소 위치 지정; top, bottom, left, right 를 사용하여 이동 가능
  - static(기준 위치): 모든 태그 default value
  - relative(상대 위치): static 위치를 기준으로 이동(normal flow 유지)
  - absolute(절대 위치): 요소를 일반 흐름에서 제거 후, 레이아웃에서 공간을 차지하지 않음(normal flow에서 벗어남),
 _static이 아닌 가장 가까운_ 부모/조상 요소를 기준으로 이동(_없을 경우 body_)
  - fixed(고정 위치): 부모 요소 관계없이 viewpoint 기준으로 이동, 스크롤 시에도 항상 같은 곳에 위치(abs와 마찬가지로 normal flow에서 벗어남)
  - sticky ~ fixed

<br/>

### CSS 원칙 정리
- Normal flow; 모든 요소는 네모(박스 모델), 좌측 상단 배치, display에 따라 크기 배치 변경
- position 으로 위치 기준 변경






