보통 JOIN을 할 때 ON 키워드를 써서 결합조건을 작성하는데  

결합하려는 두 테이블의 컬럼명이 같을 때는 USING 키워드를 사용해서 코드를 간결하게 할 수 있다.

예 :  
테이블 A  
ID|NAME|SEX
-|-|-
1|KIM|M
2|LEE|F
3|KANG|M
4|PARK|F

테이블 B  
ID|NAME|AGE
-|-|-
1|KIM|50
2|LEE|34
3|KANG|25
4|PARK|42
```sql
SELECT 
    A.ID,
    A.NAME
FROM A
JOIN B USING (NAME)
-- JOIN B ON A.NAME = B.NAME
```