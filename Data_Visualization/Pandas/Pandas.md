<!-- TOC -->

- [판다스](#%ED%8C%90%EB%8B%A4%EC%8A%A4)
    - [판다스의 개념](#%ED%8C%90%EB%8B%A4%EC%8A%A4%EC%9D%98-%EA%B0%9C%EB%85%90)
    - [데이터프레임 DataFrame](#%EB%8D%B0%EC%9D%B4%ED%84%B0%ED%94%84%EB%A0%88%EC%9E%84-dataframe)
    - [시리즈Series](#%EC%8B%9C%EB%A6%AC%EC%A6%88series)
        - [시리즈 객체](#%EC%8B%9C%EB%A6%AC%EC%A6%88-%EA%B0%9D%EC%B2%B4)
        - [시리즈 객체를 생성하면 세 가지 요소property가 생성된다.](#%EC%8B%9C%EB%A6%AC%EC%A6%88-%EA%B0%9D%EC%B2%B4%EB%A5%BC-%EC%83%9D%EC%84%B1%ED%95%98%EB%A9%B4-%EC%84%B8-%EA%B0%80%EC%A7%80-%EC%9A%94%EC%86%8Cproperty%EA%B0%80-%EC%83%9D%EC%84%B1%EB%90%9C%EB%8B%A4)
            - [데이터](#%EB%8D%B0%EC%9D%B4%ED%84%B0)
            - [인덱스](#%EC%9D%B8%EB%8D%B1%EC%8A%A4)
            - [데이터 타입](#%EB%8D%B0%EC%9D%B4%ED%84%B0-%ED%83%80%EC%9E%85)
        - [시리즈 객체는 객체의 이름을 변경할 수 있다.](#%EC%8B%9C%EB%A6%AC%EC%A6%88-%EA%B0%9D%EC%B2%B4%EB%8A%94-%EA%B0%9D%EC%B2%B4%EC%9D%98-%EC%9D%B4%EB%A6%84%EC%9D%84-%EB%B3%80%EA%B2%BD%ED%95%A0-%EC%88%98-%EC%9E%88%EB%8B%A4)
        - [시리즈 객체 생성하기](#%EC%8B%9C%EB%A6%AC%EC%A6%88-%EA%B0%9D%EC%B2%B4-%EC%83%9D%EC%84%B1%ED%95%98%EA%B8%B0)
    - [판다스의 모든 객체는 인덱스 값을 기준으로 생성된다](#%ED%8C%90%EB%8B%A4%EC%8A%A4%EC%9D%98-%EB%AA%A8%EB%93%A0-%EA%B0%9D%EC%B2%B4%EB%8A%94-%EC%9D%B8%EB%8D%B1%EC%8A%A4-%EA%B0%92%EC%9D%84-%EA%B8%B0%EC%A4%80%EC%9C%BC%EB%A1%9C-%EC%83%9D%EC%84%B1%EB%90%9C%EB%8B%A4)
    - [데이터프레임 객체](#%EB%8D%B0%EC%9D%B4%ED%84%B0%ED%94%84%EB%A0%88%EC%9E%84-%EA%B0%9D%EC%B2%B4)
        - [데이터프레임의 생성](#%EB%8D%B0%EC%9D%B4%ED%84%B0%ED%94%84%EB%A0%88%EC%9E%84%EC%9D%98-%EC%83%9D%EC%84%B1)
- [판다스 데이터 추출](#%ED%8C%90%EB%8B%A4%EC%8A%A4-%EB%8D%B0%EC%9D%B4%ED%84%B0-%EC%B6%94%EC%B6%9C)
    - [데이터 로딩](#%EB%8D%B0%EC%9D%B4%ED%84%B0-%EB%A1%9C%EB%94%A9)
    - [데이터 추출열 이름 사용](#%EB%8D%B0%EC%9D%B4%ED%84%B0-%EC%B6%94%EC%B6%9C%EC%97%B4-%EC%9D%B4%EB%A6%84-%EC%82%AC%EC%9A%A9)
    - [데이터 추출행 번호 사용](#%EB%8D%B0%EC%9D%B4%ED%84%B0-%EC%B6%94%EC%B6%9C%ED%96%89-%EB%B2%88%ED%98%B8-%EC%82%AC%EC%9A%A9)
    - [데이터 추출행, 열 모두 사용](#%EB%8D%B0%EC%9D%B4%ED%84%B0-%EC%B6%94%EC%B6%9C%ED%96%89-%EC%97%B4-%EB%AA%A8%EB%91%90-%EC%82%AC%EC%9A%A9)
    - [loc 함수](#loc-%ED%95%A8%EC%88%98)
    - [iloc 함수](#iloc-%ED%95%A8%EC%88%98)
    - [reset_index 함수로 새로운 인덱스 할당된 객체 생성](#reset_index-%ED%95%A8%EC%88%98%EB%A1%9C-%EC%83%88%EB%A1%9C%EC%9A%B4-%EC%9D%B8%EB%8D%B1%EC%8A%A4-%ED%95%A0%EB%8B%B9%EB%90%9C-%EA%B0%9D%EC%B2%B4-%EC%83%9D%EC%84%B1)
    - [drop 함수](#drop-%ED%95%A8%EC%88%98)
- [판다스 그룹별 집계](#%ED%8C%90%EB%8B%A4%EC%8A%A4-%EA%B7%B8%EB%A3%B9%EB%B3%84-%EC%A7%91%EA%B3%84)
    - [그룹별 집계 groupby](#%EA%B7%B8%EB%A3%B9%EB%B3%84-%EC%A7%91%EA%B3%84-groupby)
        - [그룹별 집계의 기본형](#%EA%B7%B8%EB%A3%B9%EB%B3%84-%EC%A7%91%EA%B3%84%EC%9D%98-%EA%B8%B0%EB%B3%B8%ED%98%95)
        - [멀티 인덱스 그룹별 집계](#%EB%A9%80%ED%8B%B0-%EC%9D%B8%EB%8D%B1%EC%8A%A4-%EA%B7%B8%EB%A3%B9%EB%B3%84-%EC%A7%91%EA%B3%84)
        - [멀티 인덱스](#%EB%A9%80%ED%8B%B0-%EC%9D%B8%EB%8D%B1%EC%8A%A4)
        - [그룹화된grouped 상태](#%EA%B7%B8%EB%A3%B9%ED%99%94%EB%90%9Cgrouped-%EC%83%81%ED%83%9C)
        - [get_group 함수](#get_group-%ED%95%A8%EC%88%98)
        - [집계 aggreagation](#%EC%A7%91%EA%B3%84-aggreagation)
        - [변환 transformation](#%EB%B3%80%ED%99%98-transformation)
        - [필터 filter](#%ED%95%84%ED%84%B0-filter)
- [판다스 병합과 연결](#%ED%8C%90%EB%8B%A4%EC%8A%A4-%EB%B3%91%ED%95%A9%EA%B3%BC-%EC%97%B0%EA%B2%B0)
    - [병합 merge](#%EB%B3%91%ED%95%A9-merge)
        - [내부 조인 inner join](#%EB%82%B4%EB%B6%80-%EC%A1%B0%EC%9D%B8-inner-join)
        - [완전 조인 full join](#%EC%99%84%EC%A0%84-%EC%A1%B0%EC%9D%B8-full-join)
        - [왼쪽 조인 left join](#%EC%99%BC%EC%AA%BD-%EC%A1%B0%EC%9D%B8-left-join)
        - [오른쪽 조인 right join](#%EC%98%A4%EB%A5%B8%EC%AA%BD-%EC%A1%B0%EC%9D%B8-right-join)
        - [내부 조인 inner join](#%EB%82%B4%EB%B6%80-%EC%A1%B0%EC%9D%B8-inner-join)
        - [left_on과 right_on 매개변수](#left_on%EA%B3%BC-right_on-%EB%A7%A4%EA%B0%9C%EB%B3%80%EC%88%98)
        - [왼쪽 조인](#%EC%99%BC%EC%AA%BD-%EC%A1%B0%EC%9D%B8)
        - [오른쪽 조인](#%EC%98%A4%EB%A5%B8%EC%AA%BD-%EC%A1%B0%EC%9D%B8)
        - [완전 조인](#%EC%99%84%EC%A0%84-%EC%A1%B0%EC%9D%B8)
        - [인덱스에 의한 병합](#%EC%9D%B8%EB%8D%B1%EC%8A%A4%EC%97%90-%EC%9D%98%ED%95%9C-%EB%B3%91%ED%95%A9)
        - [연결 concatenate](#%EC%97%B0%EA%B2%B0-concatenate)

<!-- /TOC -->


# 판다스
![](Images/2023-05-20-16-01-24.png)
## 판다스의 개념
- 파이썬의 데이터 분석 라이브러리이다.
  - 데이터 테이블(data table)을 다루는 도구이다.
- 기본적으로 넘파이를 사용한다.
  - 판다스는 넘파이를 효율적으로 사용하기 위해 인덱싱, 연산, 전처리 등 다양한 함수를 제공한다.

</br>

## 데이터프레임 (DataFrame)
- 데이터 테이블 전체 객체

</br>

## 시리즈(Series)
- 각 열 데이터를 다루는 객체

### 시리즈 객체
- 일반적으로 하나의 피쳐 데이터를 포함하는 형태이다.
- 생성된 데이터프레임 안에 포함될 수 있다.
- list, dict, ndarray 등 다양한 데이터 타입이 시리즈 객체 형태로 반환되기도 한다.

### 시리즈 객체를 생성하면 세 가지 요소(property)가 생성된다.
#### 1. 데이터
- 기존 다른 객체처럼 값을 저장하는 요소

#### 2. 인덱스
- 항상 0부터 시작하고, 숫자로만 할당하는 값이다.
- 시리즈 객체에서는 숫자, 문자열, 0 외의 값으로 시작하는 숫자, 순서가 일정하지 않은 숫자를 입력할 수도 있다.
- 시리즈 객체에서는 인덱스 값의 중복을 허용한다.

#### 3. 데이터 타입
- 넘파이의 데이터 타입과 일치한다.
- **판다스는 넘파이의 래퍼(wrapper) 라이브러리이다.**
- 넘파이의 모든 기능을 지원하고 데이터 타입도 그대로 적용한다.  


시리즈 객체는 넘파이 배열(ndarray)의 하위 클래스이다.  
넘파이가 지원하는 어떠한 데이터 타입도 지원한다.  
인덱스와 반드시 정렬되어 있을 필요는 없다.  
인덱스 값은 중복을 허용한다.  

</br>

시리즈 생성, 출력
```python
import pandas as pd #pandas 모듈 호출
import numpy as np # numpy 모듈 호출

from pandas import Series, DataFrame

list_data = [1, 2, 3, 4, 5]
list_name = ['a', 'b', 'c', 'd', 'e']
example_obj = Series(data = list_data, index = list_name)
example_obj
```
결과
```python
a 1
b 2
c 3
d 4
e 5
dtype : int64
```

</br></br>

시리즈의 인덱스 출력
```python
example_obj.index
```
결과
```python
Index(['a', 'b', 'c', 'd', 'e'], dtype = 'object')
```
</br></br>

### 시리즈 객체는 객체의 이름을 변경할 수 있다.
- 열의 이름을 지정해주는 방식
- 인덱스 이름도 추가로 지정 가능하다.

</br>

시리즈 객체의 이름과 인덱스의 이름 변경
```python
example_obj.name = 'number'
example_obj.index.name = 'id'
example_obj
```
결과
```python
id
a 1
b 2
c 3
d 4
e 5
Name : number, dtype : int64
```

</br></br>

### 시리즈 객체 생성하기
- 데이터프레임 객체를 먼저 생성하고 각 열에서 시리즈 객체를 뽑는 것이 일반적인 방법이다.
- 다양한 시퀀스형 데이터 타입으로 저장이 가능하다.

</br>

딕셔너리를 활용한 시리즈 객체 생성
```python
dict_data = {'a':1, 'b':2, 'c':3, 'd':4, 'e':5}
example_obj = Series(dict_data, dtype = np.float32, name = 'example_data')
example_obj
```
결과
```python
a 1.0
b 2.0
c 3.0
d 4.0
e 5.0
Name : example_data, dtype : float32
```
</br></br>

## 판다스의 모든 객체는 인덱스 값을 기준으로 생성된다
- 기존 데이터에 인덱스 값을 추가하면 NaN 값이 출력된다.

</br>  

기존 데이터에 인덱스를 더 추가
```python
dict_data_1 = {'a':1, 'b':2, 'c':3, 'd':4, 'e':5}
indexes = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
series_obj_1 = Series(dict_data_1, index = indexes)
series_obj_1
```
결과
```python
a 1.0
b 2.0
c 3.0
d 4.0
e 5.0
f NaN
g NaN
h NaN
dtype : float64
```
</br></br>

## 데이터프레임 객체
- 데이터 테이블 전체를 지칭하는 객체
- 넘파이 배열의 특성을 그대로 가진다
- 인덱싱 : 열과 행 각각 사용하여 하나의 데이터에 접근한다.

### 데이터프레임의 생성
- 'read_확장자'함수로 데이터 바로 로딩
  - csv나 xlsx등 스프레드시트형 확장자 파일에서 데이터 로딩

- 데이터프레임을 직접 생성
  - 딕셔너리 타입 데이터에서 **키는 열 이름**, **값은 시퀀스형 데이터 타입**을 넣어 각 열의 데이터로 만듦
  - 데이터 생성 시, 열 이름을 한정하면 해당 열만 추출 가능
  - 데이터가 존재하지 않는 열을 추가하면 해당 열에는 NaN 값들 추가

</br></br>

# 판다스 데이터 추출
## 데이터 로딩
- xlsx 형태 데이터를 호출
  - openpyxl 모듈을 설치
  - pip install openpyxl
  - read_excel 함수로 엑셀 데이터 호출
```python
import pandas as pd # pandas 모듈 호출
import numpy as np # numpy 모듈 호출
df = pd.read_excel('excel-comp-data.xlsx')
```
</br></br>


## 데이터 추출(열 이름 사용)
- head와 tail 함수 : 처음 n개 행이나 마지막 n개 행 호출
- 열 이름을 리스트 형태로 넣어 호출
  - 가장 일반적인 호출 방법이다.
  - 문자형 열 이름을 하나만 넣으면 값이 시리즈 객체로 반환된다.
  - 열 이름을 여러 개 넣으면 데이터프레임 객체로 반환된다.

```python
df[['account', 'street', 'state']].head(3)
```
</br></br>

## 데이터 추출(행 번호 사용)
- 인덱스 번호로 호출
- 기존의 리스트나 넘파이 배열(ndarray) 인덱싱과 동일
```python
df[:3]
```
</br></br>

## 데이터 추출(행, 열 모두 사용)
- 열 이름과 행 번호 함께 사용
- 데이터의 일정 부분을 사각형 형태로 잘라냄
```python
df[['name', 'stree']][:2]
```
</br></br>

## loc 함수
- 인덱스 이름과 열 이름으로 데이터 추출
- 인덱스를 0부터 시작하는 숫자 아닌 다른 값으로 변경 가능
```python
df.index = df['account']
del df['account']
df.head()
```

</br></br>

## iloc 함수
- 인덱스 번호로만 데이터 호출
- index location의 약자
```python
df.iloc[:10, :3]
```
</br></br>

## reset_index 함수로 새로운 인덱스 할당된 객체 생성
- 인덱스 이름이나 인덱스 중 편한 방법을 사용
```df_new = df.reset_index()
df_new
```
</br></br>

## drop 함수
- 특정 열이나 행을 삭제한 객체를 반환
</br></br>
</br></br>

# 판다스 그룹별 집계
## 그룹별 집계 (groupby)
- 데이터로부터 동일한 객체를 가진 데이터만 따로 뽑아 기술통계 데이터를 추출
- 엑셀의 피벗테이블(pivot table) 기능과 비슷
- 예) A반 수학 점수의 원본 데이터(raw data)를 가지고 있을 때 해당 데이터에서
  - 같은 성별을 가진 학생들의 평균 점수를 구하거나
  - 50점 이상을 받은 학생의 수를 구함
- groupby 명령어는 분할-적용-결합 과정을 가짐
  - 분할(split) : 같은 종류의 데이터끼리 나누는 기능
  - 적용(apply) : 데이터 블록마다 sum, count, mean 등 연산 적용
  - 결합(combine) : 연산 함수가 적용된 각 블록들을 합침

### 그룹별 집계의 기본형
df.groupby('Team')['Points'].sum()  
Team : 묶음의 기준이 되는 열  
Points : 적용받는 열  
sum : 적용받는 연산  

### 멀티 인덱스 그룹별 집계
- 한 개 이상의 열을 기준으로 그룹별 집계를 실행
  - 리스트를 사용하여 여러 개의 열 이름을 기준으로 넣으면 여러 열이 키 값이 되어 결과가 출력된다.
  - 계층적 인덱스(hierachical index) 형태

### 멀티 인덱스
- 한 개 이상의 열로 그룹별 집계를 수행하면 여러 열이 모두 인덱스로 반환됨  

### 그룹화된(grouped) 상태
- 분할-적용-결합 중에서 분할까지만 이루어진 상태

### get_group 함수
- 해당 키 값을 기준으로 분할된 데이터프레임 객체를 확인

### 집계 (aggreagation)
- 요약된 통계 정보를 추출
- agg 함수 : min, 넘파이 mean 등 기존 함수 그대로 적용

### 변환 (transformation)
- 해당 정보를 변환
- 키 값별로 요약된 정보가 아닌 개별 데이터 변환 지원
- 적용 시점에서는 그룹화된 상태의 값으로 적용

### 필터 (filter)
- 특정 조건으로 데이터를 검색
- 주로 filter 함수 사용
</br></br>
</br></br>

# 판다스 병합과 연결
## 병합 (merge)
- 두 개의 데이터를 특정 기준한 기준을 가지고 하나로 통합하는 작업
- SQL에서는 조인(join)이라는 표현을 더 많이 사용

### 내부 조인 (inner join)
- 키 값을 기준으로 두 테이블에 모두 존재하는 키 값의 행끼리 병합

### 완전 조인 (full join)
- 두 개의 테이블에서 각각의 행을 병합
- 두 테이블에서 동일한 키 값을 가진 행은 통합하고 두 테이블 중 하나라도 키 값이 존재하지 않는다면 존재하는 쪽의 데이터만 남겨둠

### 왼쪽 조인 (left join)
- 왼쪽 테이블의 값을 기준으로 같은 키 값을 소유하고 있는 행을 병합하고, 오른쪽 테이블에 해당 키 값이 존재하지 않는다면 해당 행은 삭제한다.

### 오른쪽 조인 (right join)
- 오른쪽 테이블의 값을 기준으로 같은 키 값을 소유하고 있는 행을 병합하고, 왼쪽 테이블에 해당 키 값이 존재하지 않는다면 해당 행은 삭제

### 내부 조인 (inner join)   
- 가장 기본적인 조인
-  집합으로 보면 양쪽의 교집합 데이터를 통합

### left_on과 right_on 매개변수
- 왼쪽 테이블과 오른쪽 테이블의 키 값이 다른 경우
- left_on과 right_on 매개변수를 사용하여 각 테이블 키 값을 입력  

### 왼쪽 조인
- 왼쪽 테이블을 기준으로 데이터를 병합
- 오른쪽 테이블에 왼쪽 테이블에 있는 키 값이 존재하지 않는다면 NaN으로 출력

### 오른쪽 조인
- 오른쪽 테이블 기준으로 데이터를 병합

### 완전 조인
- 두 테이블의 합집합을 의미
  - 양쪽에 같은 키 값이 있는 데이터는 합치고 나머지는 NaN

### 인덱스에 의한 병합
- 인덱스 값을 키 값으로 하여 두 테이블을 병합할 수 있음
- 인덱스가 의미 있는 열로 지정되어 있거나 두 데이터가 모두 순서대로 들어가 있는 경우에 사용
- right_index나 left_index 매개변수

### 연결 (concatenate)
- 두 테이블을 그대로 붙임
- 데이터의 스키마가 동일할 때 그대로 연결
- 주로 세로로 데이터를 연결
  - concat 함수 : 두 개의 서로 다른 테이블을 하나로 합침
  - append 함수 : 기존 테이블 하나에 다른 테이블을 붙임
  - append 함수는 파일을 한 개씩 합치기 때문에 두 개 이상의 데이터프레임을 합칠 때에는 concat 함수를 쓰는 것이 좋다.
