# CSS(styling)  

<br>

## CSS Box Model  

(Box model 사진)

### CSS 원칙1(Box Model)
- from **left&up** to right&down(Normal Flow)
- one box contains(content, padding, border, margin)
	- Content; 실제 내부 내용
	- Padding; **테두리 안쪽 내부 여백 요소**에 적용된 배경색, 이미지 포함
	- Border; 테두리 영역
	- Margin; 테두리 바깥 외부 여백
		- cf) margin collapse - not working(top - bottom)
	- 순서 - 상/우-좌/하 (+, %, cw)
- box-sizing; 기본적으로 content-box, 바깥 영역까지 고려하려면 'border-box'로 설정

<br>

### CSS 원칙2(display)  
* display: block
	- 줄 바꿈, 화면 width 전체 차지
	- 블록 레벨 안에 인라인 레벨 요소 들어갈 수 있음
	- 요소) div / ul, ol, li / p / hr / form 등
<br>

* display: inline
	- cotent 마크업 하고 있는 크기의 width
	- **width, height, margin-top, margin-bottom 등을 지정 X**
	- ~~상하 여백은 line-height 으로 지정 가능~~
	- 요소) span / a / img / input, label 등

* display: none
	- 화면 표시하지 않고 공간도 부여되지 않음
	- `visibility: hidden`은 공간은 차지하나 표시만 되지 않는다.

### CSS position
* static: 모든 태그의 기본 값(기준 위치)
* relative: 상대 위치
	- normal flow 유지
* absolute: 절대 위치
	- normal flow 벗어남
	- 가장 가까이 부모/조상 요소 기준(없다면 body)
* fixed: 고정 위치
	- notmal flow 벗어남
	- viewpoint 기준, 스크롤 시에도 항상 같은 곳에 위치
* sticky: 스크롤에 따라 static -> fixed

<br>

[[참고 내용]]
- emmet; 자동 완성 기능
	- ```! + tab(enter)```; html 기본 뼈대 자동완성
	- ```.class-name``` => ```<div class="class-name"></div>```
	- cf) css 환경 내에서도 가능함!

- lorem (ipsum); 라틴어, 아무 의미 없는 공간 차지용 +(단어 수) / *(단락 수)  

<br>

## CSS Layout  
<br>

### Float  
- 정의: 박스를 띄워 인라인 요소들이 주변을 wrapping 하도록 함
- 속성; none(기본값), left, right

### Flexbox
- 수직 정렬, 아이템 너비와 높이 혹은 간격을 동일하게 배치하는 어려움이 발생
- main-axis 와 cross-axis 로 틀을 만듦; `flex-direction: row`  
* Flex Container(부모 요소) - Flex Item(자식 요소)  

#### Flex 속성  
* 배치 설정
	- flex-direction; row / column / -reverse
	- flex-wrap; 영역 벗어날 경우 줄 바꿈
* 공간 분할
	- justify-content(main-axis 기준); flex-start / flex-end / center / space-between / space-around / space-evenly
	- align-content(cross-axis 기준); (위와 동일)
* 정렬 - 글씨
	- align-items(모든 아이템을 cross-axis 기준으로)
	- align-self(개별 아이템)
	- 속성; stretch(기본 값, 컨테이너 가득) / flex-start(위) / flex-end(아래) / center(가운데) / baseline(텍스트 기준에 맞춰)