# ๐ฅ ํก์ง ๋ฐฑ์ค ๋ฟ์ ๐ฅ

[![Solved.ac Profile](http://mazassumnida.wtf/api/v2/generate_badge?boj=hjb7165)](https://solved.ac/hjb7165/)
<br>

## ์์ํ ๋  : 2022๋ 12์ 30์ผ
## ๋ชฉํ : **์ค๋ฒ V**
### <br>๋ฐฑ์ค ํ์ด ์ผ๊ธฐ
---
๋ ์ง : 2022.12.30.  
ํผ ๋ฌธ์  : test  
```python
print("Hello, world!")
```
print๋ก ์ถ๋ ฅ๋ง ํ๋ฉด ๋๋ค.

---
๋ ์ง : 2023.01.05.  
ํผ ๋ฌธ์  : 2750    
```python
N = int(input())
l = []
for i in range(N):
    a = int(input())
    l.append(a)

l.sort()

for i in l:
    print(i)
```
์ ๋ ฌ ์๊ณ ๋ฆฌ์ฆ์ ์จ์ผํ์ง๋ง ์ผ๋จ์ ๋ด์ฅํจ์ .sort()๋ฅผ ์ด์ฉํด์ ํ์๋ค.

---
๋ ์ง : 2023.01.05.  
ํผ ๋ฌธ์  : 2587  
```python
# ํ๊ท ๊ณผ ์ค์๊ฐ ๊ตฌํ๊ธฐ

l = []
sum = 0
for i in range(5):
    a = int(input())
    sum+=a
    l.append(a)

l.sort()

print(int(sum/5))
print(l[2])
```
2750๋ฒ๊ณผ ๊ฐ์ ๋ฐฉ์์ผ๋ก .sort()๋ฅผ ์ด์ฉํด์ ์ ๋ ฌํ๋ค
```python
import sys
l = [int(sys.stdin.readline().strip()) for i in range(5)]

l.sort()

print(int(sum(l)/5))
print(l[2])
```
sys.stdin.readline()๊ณผ list comprehension์ ์ด์ฉํด์ appendํจ์์ input()์ ์ฐ์ง ์๊ณ  2587๋ฒ์ ๋ค์ ํ์ด๋ณด์๋ค.   

---
๋ ์ง : 2023.01.05.  
ํผ ๋ฌธ์  : 2751  
```python
import sys
N = int(sys.stdin.readline())
l = [int(sys.stdin.readline().strip()) for i in range(N)]

l.sort()

for i in l:
    print(i)
```
## :rocket: sys.stdin.readline()  
_input()๋์  sys.stdin.readline()๋ฅผ ์ฌ์ฉํด์ผํ๋ค!!!_   
๋๋๊ฒ๋ ๋ชจ๋  ์๋ ฅ ์ค input()์ด ๊ฐ์ฅ ๋๋ฆฌ๋ค๊ณ  ํ๋ค.  
2751์์๋ ๋ฌด๋ ค 1,000,000๊ฐ ์ดํ์ ์ซ์๋ฅผ ์๋ ฅ๋ฐ์์ผ ํ๋ฏ๋ก for๋ฌธ์ ๋๋ฉด์ ๊ณ์ input()์ผ๋ก๋ง ๋ฐ๋ค๋ณด๋ ์๊ฐ์ด๊ณผ ๋ฌธ์ ๊ฐ ๋ฐ์ํ์๋ค.  
##### ์์ผ๋ก๋ sys.stdin.readline()์ ์ต๊ดํํ์!  
**์ฌ์ฉ๋ฒ์ <https://velog.io/@yeseolee/Python-%ED%8C%8C%EC%9D%B4%EC%8D%AC-%EC%9E%85%EB%A0%A5-%EC%A0%95%EB%A6%ACsys.stdin.readline>๋ฅผ ์ฐธ๊ณ ํ์๋ค.**  

```python
l = [int(sys.stdin.readline().strip()) for i in range(N)]
```
์ ์ฝ๋๋ N๊ฐ์ ์ซ์๋ฅผ ์ฌ๋ฌ์ค๋ก ๋ฐ์์ค ๋ ์ฌ์ฉํ๋ค  
์ด ๋, int()๋ ๊ผญ ๋ถ์ฌ์ค์ผํ๋ค!  
int๋ฅผ ๋ถ์ด์ง ์์ผ๋ฉด ์๋ ฅ์ ๋ฌธ์์ด๋ก ๋ฐ๊ธฐ๋๋ฌธ์ 1 14 2๋ฅผ ์ค๋ฆ์ฐจ์ ์์ผฐ๋๋ 1 14 2๋ก ์ถ๋ ฅ๋์๋ค   

---
๋ ์ง : 2023.01.05.  
ํผ ๋ฌธ์  : 2751  
```python
N, k = map(int, input().split())

x = list(map(int, input().split()))
x.sort(reverse=True)

print(x[k-1])   
```
ํ ์ค์ ์ฌ๋ฌ๊ฐ์ ๋ณ์๋ฅผ ์๋ ฅ๋ฐ๊ฑฐ๋, ์ฌ๋ฌ๊ฐ์ ์ซ์๋ค์ for๋ฌธ์ ์ด์ฉํ์ง ์๊ณ  ์๋ ฅ๋ฐ๊ธฐ ์ํด mapํจ์๋ฅผ ํ์ฉํ  ์ ์๋ค.  
### <br>mapํจ์
```python
map(์ ์ฉ์ํฌ ํจ์, ๋ฆฌ์คํธ๋ ํํ ๋ฑ)
```
mapํจ์์ ๋ฐํ๊ฐ์ map๊ฐ์ฒด์ด๋ฏ๋ก ํ ๋ณํ ํ์!!  

---
๋ ์ง : 2023.01.05.  
ํผ ๋ฌธ์  : 2108  
```python
# ์ฐ์ ํ๊ท , ์ค์๊ฐ, ์ต๋น๊ฐ, ๋ฒ์
import sys
from collections import Counter

N = int(sys.stdin.readline())
l = [int(sys.stdin.readline().strip()) for i in range(N)]

l.sort()

#์ต๋น๊ฐ๊ตฌํ๋ ํจ์
def Most(li, n):
    if n!=1:
        counter = Counter(l).most_common(2) 
        # type(counter) : list, counter์ ์์๋ tuple
        if counter[0][1] == counter[1][1]:
            return counter[1][0]
        else:
            return counter[0][0]
    else:
        return li[0]
        
print(round(sum(l)/N)) # ์ฐ์ ํ๊ท  
print(l[int(N/2)]) # ์ค์๊ฐ
print(Most(l, N)) #์ต๋น๊ฐ
print(l[N-1]-l[0]) #๋ฒ์
```
์ฐฝ์ํ ์์ ๋ ๋ฐฐ์ด **counterํจ์**๋ก ํ์๋ค.  
counterํจ์๋ ์ฃผ๋ก ๋ฌธ์์ด์์ ๋ฌธ์์ ๊ฐ์๋ฅผ ์ ๋ ์ฐ์ด๋๋ฐ ์ด๋ ๊ฒ ๋ฆฌ์คํธ ์์ ์ซ์๋ค๋ก๋ ๋น๋๋ฅผ ์ฒดํฌํ  ์ ์์๋ค. ๋ค๋ฅธ ํ์ด๋ค๋ ์ฐพ์๋ด์ผํ ๊ฒ ๊ฐ๋ค.  

---
๋ ์ง : 2023.01.05.  
ํผ ๋ฌธ์  : 2563
```python
import sys
import numpy as np

N = int(sys.stdin.readline())
A = np.zeros((100,100))

for i in range(N):
    a,b = map(int, sys.stdin.readline().split())
    A[a-1:a+9, b-1:b+9] = 1

print(int(A.sum()))
```
๋ฐฑ์ค์์๋ ์ธ๋ถ ๋ผ์ด๋ธ๋ฌ๋ฆฌ๋ฅผ ์ง์ํ์ง ์๋ ๊ด๊ณ๋ก numpy๋ฅผ ์ฌ์ฉํ๋ฉด ๋ฐํ์์๋ฌ๊ฐ ๋๋ค๊ณ  ํ๋ค :sob: ๊ทธ๋์ ์๊พธ
 ์๋ฌ๊ฐ ๋ฌ๋ ๊ฒ์...์๋..
```python
import sys

N = int(sys.stdin.readline())
A = [[0 for i in range(100)] for j in range(100)]

sum = 0
for i in range(N):
    a,b = map(int, sys.stdin.readline().split())
    for j in range(a-1,a+9):
        for k in range(b-1,b+9):
            if A[j][k] == 0:
                sum+=1
                A[j][k] = 1
                
print(sum)
```
๊ฒฐ๊ตญ ์ผ์คfor๋ฌธ์ผ๋ก ์ผ์ผ์ด 1์ ์ฑ์๋ฃ์์ง๋ง ์ถํ ๋ค๋ฅธ ํ์ด๋ ์ฐพ์๋ด์ผํ  ๊ฒ ๊ฐ๋ค

---
๋ ์ง : 2023.01.07
ํผ ๋ฌธ์  : 1181, 10814, 18870

---
๋ ์ง : 2023.01.09
ํผ ๋ฌธ์  : 1158(์ฐ๊ฒฐ๋ฆฌ์คํธX)

---
๋ ์ง : 2023.01.12
ํผ ๋ฌธ์  : 10872, 10870, 25501

---
๋ ์ง : 2023.01.17
ํผ ๋ฌธ์  : 2562, 10818, 10871

---
๋ ์ง : 2023.01.20
ํผ ๋ฌธ์  : 10828, 3052, 1002, 5597, 10989, 9012, 10773, 4949

---
๋ ์ง : 2023.01.22
ํผ ๋ฌธ์  : 1747, 1546, 1652, 8958

---
๋ ์ง : 2023.01.24
ํผ ๋ฌธ์  : 1874, 18258, 2566, 2738
1. 17298-> ์คํ์ผ๋ก ๋ค์
2. ๊ทธ๋ํ์ด๋ก  ๊ณต๋ถํ๊ธฐ

---
๋ ์ง : 2023.01.26
ํผ ๋ฌธ์  : 2164

---
๋ ์ง : 2023.02.06
ํผ ๋ฌธ์  : 1934, 2609, 1037

---
๋ ์ง : 2023.02.12
ํผ ๋ฌธ์  : 1676, 1010, 11051, 11050, 3036

---
๋ ์ง : 2023.02.13
ํผ ๋ฌธ์  : 2004