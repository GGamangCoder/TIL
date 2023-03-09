## CSS Layout 잡아주기  

- Recap / 다른 표현 뭐 있었던거 같은데
  - Box model
  - Normal flow?

### Float  
- Float 속성) none / left / right
- 공간에 띄워주기
- 과거에 필수적으로 활용되었으나 현재는 잘 사용하지 않음 -> 최근에는 Flexbox, Grid 등을 사용
- 원하는 요소를 지정하여 배치할 수 있음  


### Flexbox  
[등장 배경]  
: Normal Flow 적용 안되는 경우; (Float / Position)수직 정렬, 너비나 높이 혹은 간격을 동일하게 배치할 경우  

- CSS Flexible Box Layout; 행과 열 형태로 아이템들을 배치하는 1차원 레이아웃 모델
- 축; 메인 축 & 교차(직교) 축 - 쌓이는 방향에 따라
- 구성 요소; 부모 요소(Container) & 자식 요소(Item)

#### Flex 속성
- 배치 설정; flex-direction / flex-wrap &nbsp;&nbsp;&nbsp;&nbsp; - 두 가지 shorthand 작성 가능
  1. flex-direction; row(default), row-reverse, column, column-reverse
  2. flex-wrap; 줄 바꿈 - 공간 넘어갈 경우 새로운 라인에서 배치(컨테이너 영역 內)
- 공간 분할; justify-content(main) / align-content(cross)
  1. justify-content; Main axis 기준 공간 배분 = flex-start, flex-end, center, space-between, space-around, space-evenly
  2. align-content; Cross axis 기준 공간 배분 = (위와 동일)
- 정렬; align-items(모든 아이템, cross axis 기준) / align-self(개별 아이템)
  1. align-items; **모든** 아이템 cross axis 기준 = stretch, flex-start, flex-end, center, baseline
  2. align-self; **개별** 아이템 위와 동일
- 기타 속성; flex-grow, order  
 cf) align에 대하여 content / items 차이는 content는 전체에 대해서, items는 각각의 아이템을 정렬해주는 차이가 있다.
