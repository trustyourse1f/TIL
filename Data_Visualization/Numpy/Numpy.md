# Numpy

현실 세계의 다양한 데이터는 배열 형태로 표현할 수 있다.  
기계 학습에서는 파이썬의 기본 리스트로 충분하지 않다.  
데이터를 처리할 때는 리스트와 리스트 간의 연산이 가능해야 하는데 파이썬의 기본 리스트는 이것을 지원하지 않기 때문이다.  
연산 속도도 중요하기 때문에 데이터 과학자들은 **기본 리스트 대신에 넘파이(Numpy)를 선호한다.**  

## 넘파이의 개념
- 파이썬의 고성능 과학 계산용 라이브러리
- 벡터나 행렬 같은 선형대수의 표현법을 코드로 처리
- 사실상의 표준 라이브러리
- **다차원 리스트나 크기가 큰 데이터를 효과적으로 처리하는데 유리하다.**
- 파이썬을 위한 행렬(matrix) 라이브러리

## 특징
- 과학적인 계산을 위해서 만들어진 형태
- **정적 할당**의 구성 방식으로 사용하기 위하여 만들어짐
- **행렬 연산 특화**
- **일반 리스트에 비해 빠르고, 메모리를 효율적으로 사용**
- 데이터를 메모리에 할당하는 방식이 기존과 다름
- 반복문을 사용하지 않음
- 연산할 때 **병렬로 처리**
- 함수를 한 번에 많은 요소에 적용
- 반복문 없이 데이터 배열에 대한 처리를 지원하여 빠르고 편리
- 선형대수와 관련된 다양한 기능을 제공
- C, C++, 포트란 등의 언어와 통합이 가능

## 성능
- 넘파이의 텐서 연산의 장점
  - C와 유사한 형태로 메모리를 관리하면서 C와 같은 연산 속도로 계산할 수 있다.
  - 메모리 구조상 요소들이 붙어있기 때문
  - 파이썬의 가장 큰 특징인 동적 타이핑을 포기했지만, C로 구현되어 있어 배열 연산에 있어 매우 큰 성능적 우위 확보
  - 대용량 배열 연산에서 넘파이가 사실상 표준으로 사용됨
- 연결 연산처럼 여러 배열을 붙이는 연산에서는 일반적인 리스트에 비해 느림
  - 필요할 때마다 메모리 탐색 과정으로 새로운 공간을 잡아야 하기 때문



## 넘파이 배열(ndarray) : 넘파이에서 텐서 데이터를 다루는 객체

## 텐서(tensor) : 선형대수의 데이터 배열
- 랭크(rank)에 따라 이름이 다름  

랭크(rank)|이름|예
-|-|-
0|스칼라|7
1|벡터|[10, 10]
2|행렬|[[10, 10], [15, 15]]
3|3차원 텐서|[[[1, 5, 9], [2, 6, 10]],[[3, 7, 11], [4, 8, 12]]] 
n|n차원 텐서|

## 배열 생성
- np.array 함수 사용하여 배열 생성
    ```python
    import numpy as np
    test_array = np.array([1, 4, 5, 6], float)
    ```
    - 매개변수 1: 배열 정보
    - 매개변수 2: 넘파이 배열로 표현하려는 데이터 타입

- Numpy 형식으로 배열의 원소를 입력할 때는 반드시 리스트 형식으로 입력
  ```python
  test_array = np.array([1, 4, 5, 8], float) (o)
  test_array = np.array(1, 4, 5, 8)          (x)
  ```

## 파이썬 리스트와 넘파이 배열의 차이점
- 텐서 구조에 따라 배열 생성
  - 배열의 모든 구성 요소에 값이 존재해야 한다.
  ```python
  import numpy as np
  test_list = [[1, 4, 5, 8], [1, 4, 5]]
  np.array(test_list, float) # ValueError
  ```
  - 동적 타이핑을 지원하지 않음
    - 하나의 데이터 타입만 사용한다.
  - 데이터를 메모리에 연속적으로 나열한다.
    - 각 값 메모리 크기가 동일하다.
    - 검색이나 연산 속도가 리스트에 비해 훨씬 빠르다.

데이터의 특징을 출력하는 요소(property)는 dtype과 shape
- dtype은 넘파이 배열의 데이터 타입을 반환
- shape는 넘파이 배열에서 객체(object)의 차원(dimension)에 대한 구성 정보를 반환
- 최대 차원 `np.ndim`
- 원소 개수 `np.size`
  
매개변수 `dtype`으로 넘파이 배열의 데이터 타입 지정
- 변수가 사용하는 메모리 크기가 정해짐
- dtype을 실수형인 float으로 지정한다면 모든 데이터가 실수형으로 저장
- itemsize 요소(property)로 넘파이 배열에서 각 요소가 차지하는 바이트(byte) 확인
  - np.float64로 dtype을 선언하면 64비트, 즉 8바이트 차지
  - np.float32로 dtype을 선언하면 32비트, 즉 4바이트 차지

### reshpape
- 배열을 원하는 모양으로 생성 및 변형
```python
x = np.array([[1, 2, 5, 8], [1, 2, 5, 8]])
x.reshape(-1, )
```
[1, 2, 5, 8]  
[1, 2, 5, 8]       -> [1, 2, 5, 8, 1, 2, 5, 8]

- 반드시 전체 요소의 개수는 통일
```python
x = np.array([0, 1, 2, 3, 4, 5, 6, 7])
x.reshape(2, 2) (X)
```

- -1을 사용하면 나머지 차원의 크기를 지정했을 때 전체 요소의 개수를 고려하여 마지막 차원이 자동으로 지정됨
```python
x = np.array([0, 1, 2, 3, 4, 5, 6, 7])
x.reshape(2, -1, )
x.reshape(2, 2, -1, )
```

### flaten 함수는 데이터 그대로 1차원으로 변경
- 데이터의 개수는 그대로 존재
- 배열의 구조만 변한다.
```python
x = np.array([0, 1, 2, 3, 4, 5, 6, 7])
x.reshape(2, 2, 2)
x.flatten()
```

## 인덱싱(indexing)
- 리스트에 있는 값의 상대적인 주소(offset)로 값에 접근
- 넘파이 배열의 인덱스 표현에는 ','을 지원
  - '[행][열]' 또는 '[행,열]' 형태
- 3차원 텐서 이상은 shape에서 출력되는 랭크 순서대로 인덱싱에 접근
``` python
x = np.array([[1. 2. 3], [4, 5, 6]], int)
x
--------------------------------------------
array([[1, 2, 3],
        [4, 5, 6]])
```

```python
x[0][0]
------------------------
1
```
```python
x[0, 2]
------------------------
3
```
```python
x[0, 1] = 100
x
--------------------------------------------
array([[1, 100, 3],
        [4, 5, 6]])
```

## 슬라이싱(slicing)
- 인덱스를 사용하여 리스트 일부를 잘라내어 반환
- 넘파이 배열은 행과 열을 나눠 슬라이싱 가능
- 증가값(step) : 리스트에서 데이터의 요소를 호출할 때 데이터를 건너뛰면서 반환
  - [시작 인덱스: 마지막 인덱스: 증가값] 형태
  - 각 랭크에 있는 요소별로 모두 적용할 수 있음
  - ex) [: 2, : ] 0행부터 1행까지, 전체 열
```python
x = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]], int)
x[:, 2:] # 전체 행의 2열 이상
----------------------------------------
array([[3. 4. 5],
        [8, 9, 10]])
```
```python
x[1, 1:3] # 1행의 1열~2열
--------------------------
array([7, 8])
```
```python
x[1:3] # 1행~2행 전체
--------------------------
array([[6, 7, 8, 9. 10]])
```
```python
x = np.array([[0, 1, 2, 3, 4], [5, 6, 7, 8, 9], [10, 11, 12, 13, 14]])
x[:, ::2]
------------------------------------------------
array([[0, 2, 4],
        [5, 7, 9],
        [10, 12, 14]])
```
```python
x[::2, ::3]
------------------------------------------------
array([[0, 3],
        [10, 13]])
```


## 다양한 함수들
### arange 함수
- range 함수와 같이 차례대로 값을 생성한다.
- (시작 인덱스, 마지막 인덱스, 증가값)으로 구성
- range함수와 달리 증가값에 실수형이 입력되어도 값을 생성할 수 있다.
- 소수점 값을 주기적으로 생성할 때 유용하다.
```python
np.arange(10)
--------------------------------------
array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
```
```python
np.arange(-5, 5)
-------------------------------------------
array([-5, -4, -3, -2, -1, 0, 1, 2, 3, 4])
```
```python
np.arange(0, 5, 0.5)
------------------------------------------------
array([0, 0.5, 1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5])
```

### ones 함수
- 1로만 구성된 넘파이 배열을 생성
- 사전에 shape 값을 넣어서 원하는 크기의 넘파이 배열 생성

### zeors 함수
- 0으로만 구성된 넘파이 배열을 생성

### empty 함수
- 활용 가능한 메모리 공간 확보하여 반환
- ones와 zeros는 먼저 shape의 크기만큼 메모리를 할당하고 그곳에 값을 채움
- 해당 메모리 공간에 값이 남았을 경우 그 값을 함께 반환한다.
- empty는 메모리 초기화를 하지 않아 생성될 때마다 다른 값을 반환한다.

생성 시점에서 dtype을 지정해주면 해당 데이터 타입으로 배열 생성

```python
imoport numpy as np
arr = np.zeros((2, 3))
```
```python
arr = np.arange(1, 101, 2)
```

### ones_like 함수
- 기존 넘파이 배열과 같은 크기로 만들어 내용을 1로 채운다.

### zeros_like 함수
- 기존 넘파이 배열과 같은 크기로 만들어 내용을 0으로 채운다.

### empty_like 함수
- 기존 넘파이 배열과 같은 크기로 만들어 빈 상태로 만든다.

### identity 함수
- 단위 행렬(i행렬)을 생성한다.
- 매개변수 n으로 nxn 단위행렬을 생성한다.

### eye 함수
- 시작점과 행렬 크기를 지정, 단위행렬을 생성한다.
- N은 행의 개수, M은 열의 개수를 지정한다.
- k는 열의 값을 기준으로 하는 시작 인덱스이다.

### diag 함수
- 행렬의 대각성분 값을 추출한다.
- k는 열의 값을 기준으로 하는 시작 인덱스이다.

### uniform 함수 : 균등분포 함수
- np.random.uniform(최솟값, 최댓값, 데이터개수)
```python
np.random.uniform(0, 5, 10)
-------------------------------------------
array([3.87101195, 0.122632269, 0.65361498,
0.55792293, 3.64577442, 0.93322468, 3.1913397, 1.82159678,
3.64401469])
```

### normal 함수 : 정규분포 함수
- np.random.normal(평균값, 분산, 데이터개수)
```python
np.random.normal(0, 2, 10)
-------------------------------------------
array([4.92446265, -2.4753182, -2.12734589,
-2.75839296, -0.22365806, -0.93325909, 1.81593553,
1.74506567, 2.20788194, 1.42156357])
```

### 연산 함수(operation function)
- 배열 내부 연산을 지원하는 함수

### 축(axis)
- 배열의 랭크가 증가할 때마다 새로운 축이 추가되어 차원 증가

### sum 함수
- 각 요소의 합을 반환
- sum 함수를 랭크가 2이상인 배열에 적용할 때 축으로 연산의 방향을 설정

```python
import numpy as np
test_array = np.arange(1, 11)
test_array.sum()
------------------------------
55
```
```python
test_array = np.arange(1, 13).reshape(3, 4)
test_array
--------------------------------------------
array([[1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]])
```
```python
test_array.sum(axis=0)
----------------------
array([15, 18, 21, 24])
```
```python
test_array.sum(axis=1)
----------------------
array([10, 26, 42])
```

```python
test_array = np.arange(1, 13).reshape(3, 4)
third_order_tensor = np.array([test_array, test_array, test_array])

third_order_tensor.sum(axis=0)
------------------------------------------------
array([[3, 6, 9, 12],
    15, 18, 21, 24],
    [27, 30, 33, 36])
```
```python
third_order_tensor.sum(axis=1)
-------------------------------
array([[15, 18, 21, 24],
    [15, 18, 21, 24],
    [15, 18, 21, 24]])
```
```python
third_order_tensor.sum(axis=2)
--------------------------------
array([[10, 26, 42],
    [10, 26, 42],
    [10, 26, 42]])
```
```python
test_array = np.arrange(1, 13).reshape(3, 4)
test_array
----------------------------------------------
array([[1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]])
```
```python
test_array.mean(axis=1) # axis=1 기준으로 평균 연산
------------------------------------------------
array([2.5, 6.5, 10.5])
```
```python
test_array.std() # 전체 값에 대한 표준편차 연산
-----------------------------------------
3.452052529534663
```
```python
np.sqrt(test_array) # 각 요소에 제곱근 연산 수행
--------------------------------------------
array([[1., 1.41421356, 1.73205081, 2],
    [2.23606798, 2.44948974, 2.64575131, 2.82842712],
    [3., 3.16227766, 3.31662479, 3.46410162]])
```

### 연결 함수(concatenation functions)
- 두 객체간의 결합을 지원하는 함수

### vstack 함수
- 배열을 수직으로 붙여 하나의 행렬을 생성한다.

### hstack 함수
- 배열을 수평으로 붙여 하나의 행렬을 생성한다.

### concatenate 함수
- 축을 고려하여 두 개의 배열을 결합한다.
- 스택(stack) 계열의 함수와 달리 생성될 배열과 소스가 되는 배열의 차원이 같아야 한다.
- 두 벡터를 결합하고 싶다면 해당 벡터를 일단 2차원 배열 꼴로 변환한 후에 행렬로 나타내야 한다.
```python
v1 = np.array([1, 2, 3, 4]).reshape(2, 2)
v2 = np.array([[5, 6]]).T
v1
-----------------------------
array([[1, 2],
        [3, 4]])
```
```python
v2
------------------------------
array([[5],
    [6]])
```
```python
np.concatenate((v1, v2), axis=1)
---------------------------------
array([[1, 2, 5],
    [3, 4, 6]])
```

### 사칙연산 함수
- 넘파이는 파이썬과 동일하게 배열 간 사칙연산을 지원한다.
  - 행렬과 행렬, 벡터와 벡터 간 사칙연산이 가능하다.
- 같은 배열의 구조일 때 요소별 연산(element-wise operation)
  - 요소별 연산 : 두 배열의 구조가 동일할 경우 같은 인덱스 요소들끼리 연산


### 배열 간의 곱셈에서는 요소별 연산과 벡터의 내적(dot product) 연산이 가능하다.
- 벡터의 내적 : 두 배열 간의 곱셈
- 두 개의 행렬에서 첫 번째 행렬의 열 크기와 두 번째 행렬의 행 크기가 동일해야 한다.
- mxn 행렬과 nxl행렬, 벡터의 내적 연산을 하면 mxl 행렬이 생성 된다.

### dot 함수
- 벡터의 내적 연산을 수행

### 브로드캐스팅 연산(broadcasting operations)
- 하나의 행렬과 스칼라 값들 간의 연산이나 행렬과 벡터 간의 연산
  - 방송국의 전파가 퍼지듯 뒤에 있는 스칼라 값이 모든 요소에 퍼지듯이 연산  
  예 : [1, 2, 3]   &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[4, 5, 6]  
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[4, 5, 6] &nbsp;&nbsp;&nbsp;&nbsp;+ 3&nbsp;&nbsp;&nbsp; -> &nbsp;&nbsp;[7, 8, 9]

### 비교 연산
- 연산 결과는 항상 불린형(boolean type)을 가진 배열로 추출
- 브로드캐스팅 비교 연산
  - 하나의 스칼라 값과 벡터 간의 비교 연산은 벡터 내 전체 요소에 적용
  ```python
  import numpy as np
  x = np.array([4, 3, 2, 8, 5])
  x > 3
  --------------------------------------
  array([True, False, False, True, True])
  ```
- 요소별 비교 연산
  - 두 개의 배열 간 배열의 구조(shape)가 동일한 경우
  - 같은 위치에 있는 요소들끼리 비교 연산
  ```python
  x = np.array([1, 3, 0])
  y = np.array([2, 1, 7])
  x > y
  ------------------------
  array([False, True, False])
  ```

### all 함수
- 배열 내부의 모든 값이 참일 때는 True
- 하나라도 참이 아닐 경우에는 False를 반환
- and 조건을 전체 요소에 적용
  
### any 함수
- 배열 내부의 값 중 하나라도 참일 때는 True
- 모두 거짓일 경우 False를 반환
- or 조건을 전체 요소에 적용

### where 함수
- 배열이 불린형으로 이루어졌을 때 참인 값들의 인덱스를 반환
```python
x = np.array([4, 6, 7, 3, 2])
x > 5
-------------------------------
array([False, True, True, False, False])
```
```python
np.where(x>5)
-----------------------------------
(array([1, 2], dtype=int64),)
```
```python
x = np.array([4, 6, 7, 3, 2])
np.where(x>5, 10, 20)
-----------------------------------
array([20, 10, 10, 20, 20])
```

### argsort
- 배열 내 값들을 작은 순서대로 인델스를 반환

### argmax
- 배열 내 값들 중 가장 큰 값의 인덱스를 반환

### argmin
- 배열 내 값들 중 가장 작은 값의 인덱스를 반환

### 불린 인덱스(boolean index)
- 배열에 있는 값들을 반환할 특정 조건을 불린형의 배열에 넣어서 추출
- 인덱스에 들어가는 배열은 불린형이어야 함
- 불린형 배열과 추출 대상이 되는 배열의 구조가 같아야 함
```python
x = np.array([4, 6, 7, 3, 2])
x > 3
--------------------------------
array([True, True, True, False, False])
```
```python
cond = x > 3
x[cond]
------------------------------
array([4, 6, 7])
```
```python
x.shape
----------
(5,)
```
```python
cond.shape
-----------
(5,)
```

### 팬시 인덱스 (fancy index)
- 정수형 배열의 값을 사용하여 해당 정수의 인덱스에 위치한 값을 반환한다.
- 인덱스 항복에 넣을 배열은 정수로만 구성되어야 한다.
- 정수 값의 범위는 대상이 되는 배열이 가지는 인덱스의 범위 내 대상이 되는 배열과 인덱스 배열의 구조(shape)가 같을 필요는 없다.
```python
x = np.array([4, 6, 7, 3, 2])
cond = np.array([1, 2, 0, 2, 2, 2,], int)
x[cond]
---------------------------------------------
array([6, 7, 4, 7, 7, 7])
```
```python
x.take(cond)
------------------------------
array([6, 7, 4, 7, 7, 7])
```
```python
x = np.array([[1, 4], [9, 16]], int)
a = np.array([0, 1, 1, 1, 0, 0], int)
b = np.array([0, 0, 0, 1, 1, 1], int)
x[a, b]
--------------------------------------
array([1, 9, 9, 16, 4, 4])
```