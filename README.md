# get-school-timetable  
컴시간알리미 크롤링 라이브러리(Python)  
selenium과 Chrome Webdriver를 필요로 합니다.  
추가적으로 멀티프로세싱은 pathos(멀티프로세싱, 필수 아님)를 필요로 합니다.
  
## 주의!! loading_timetable 함수 2번 이상 사용시 멀티프로세싱 사용 필수
그냥 2개 이상 하면 그중에 하나만 됩니다..

  
## install selenium
```
pip install selenium
```
## install pathos
```
pip install pathos
```

## 사용 예시
### 파이썬 코드
```
from getTime import loading_timetable

# 학교 이름 정확히/학년-반 순으로
sub_list = loading_timetable('퇴계원중학교', '3-6')

# 배열이 아닌 딕셔너리(배열을 포함한 딕셔너리). 첫번째 key값은 '월', '화', '수' 등으로 입력.
# 배열은 숫자 0부터.(1교시 -> 0, 2교시 -> 1)
print(sub_list['월'][0])  # 월요일 1교시 과목은?

print(sub_list)  # 전체 시간표(일주일) 출력, 형식은 딕셔너리
```
### 출력값
```
#(print(sub_list['월'][0]) 
미술
print(sub_list)
{'월': ['미술', '사회', '영어', '국어', '중국', '창체', ''],
 '화': ['국어', '영어', '체육', '기가', '사회', '과학', '수학'],
 '수': ['미술', '사회', '영어', '국어', '중국', '창체', ''], 
 '목': ['중국', '영어', '수학', '국어', '과학', '역사', '음악'], 
 '금': ['체육', '기가', '중국', '창체', '', '', '']}
```
