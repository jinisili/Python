# %%

# 리스트와 반복문
nums = [1,2,3,4,5]

# 값만 참조하고 싶은 경우
for n in nums:
    print(n)

# 인덱스를 통해서 리스트 참조
# - 위치 찾을 때
# - 리스트 수정
for i in range(len(nums)):
    print(nums[i])

# 리스트의 특정 요소 삭제
# ex) 짝수만 삭제

# 아래처럼 하면 오류
# for i in range(len(nums)):
#     if nums[i] % 2 == 0:
#         del nums[i]
# print(nums)

# 삭제시 인덱스를 거꾸로 참조
for i in range(len(nums)-1, -1, -1):
    if nums[i] % 2 == 0:
        del nums[i]
print(nums)

# while문 활용
while any(i%2==0 for i in nums): # 짝수인 것이 하나라도 있는 경우
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            del nums[i]
            break # 하나씩 삭제

# 값과 인덱스를 동시에 얻고 싶은 경우
for i, num in enumerate(nums):
    print(i, num)

# %%

# 문제
# 입력된 정수 자리수별로 더하기
num = 12345

result = 0
for i in str(num):
    result += int(i)
print(result)

result = 0
while num:
    mok, res = divmod(num, 10)
    result += res
    num = mok
print(result)

# %%

# 문제
# 달력 출력 예제
# 1월 - 1일, 2일, ... , 31일
# 2월 - 1일, 2일, ... , 28일
# ...
# 12월 - 1일, 2일, ... , 31일
lastDayList = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

for i, days in enumerate(lastDayList):
    print(f'{i+1}월 - ', end='')
    for day in range(1, days):
        print(f'{day}일', end=', ')
    print(f'{day+1}일')

# %%

# 문제
# 3,6,9 게임
for i in range(1, 51):
    cnt = str(i).count('3') + str(i).count('6') + str(i).count('9')
    result = '짝'*cnt if cnt else i
    print(result, end=' ')

# %%

# 소수 찾기
# 2, 3, 5, 7, 11
num = 6
for i in range(2, int(num**0.5)+1):
    if not num % i:
        print(f'{num}은 소수가 아닙니다')
        break
else:
    print(f'{num}은 소수입니다')


# %%

# 최대공약수
# 두 수 a,b의 최대공약수는 b와 (a를 b로 나눈 나머지)의 최대 공약수와 같다.
# 위 성질을 반복적으로 적용해서 결국 (a를 b로 나눈 나머지)가 0이 되는 시점의 나누는 수가 최대 공약수(b)이다.
def gcd(a, b):
    while b :
        a, b = b, a % b
    return a
print(gcd(18, 48))

# 최대공배수
# a*b // 최대 공약수
def gcm(a, b):
    return a*b // gcd(a,b)
print(gcm(18, 48))

# %%

# 셋
fruits = ['사과', '사과', '포도', '귤']
fruits_set = set(fruits)
fruits_set = {f for f in fruits} # 셋 컴프리헨션
print(fruits_set)

for f in fruits_set:
    print(f)

# %%

# 딕셔너리
fruits = ['사과', '포도', '귤']
nums = [100, 300, 50]
fruits_dict = {k:v for k, v in zip(fruits, nums)} # 딕셔너리 컴프리헨션
print(fruits_dict)

# 딕셔너리와 반복문
for key in fruits_dict:
    print(key, fruits_dict[key])

for key in fruits_dict.keys():
    print(key, fruits_dict[key])

for val in fruits_dict.values():
    print(val)

for key, val in fruits_dict.items():
    print(key, val)

# 딕셔너리와 리스트
score_dict = {'국어': [], '수학': []}
score_dict['국어'].append(30)   
score_dict['국어'].append(60)
print(score_dict)

print(score_dict.get('영어', []))
print(score_dict)

# 영어라는 key가 없을 때
# setdefault는 반환을 해줘서 append가 가능
score_dict.setdefault('영어', []).append(50)
print(score_dict)

# setdefault가 없었다면
if '과학' in score_dict:
    score_dict['과학'].append(60)
else:
    score_dict['과학'] = [60]

# %%

# 내장 라이브러리
# defaultdict : 일반 딕셔너리와 달리 존재하지 않는 키에 접근할 때 기본값을 반환
from collections import defaultdict

s = [('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]
d = defaultdict(list)
print(d)
for k, v in s:
    d[k].append(v)

print(sorted(d.items()))

# %%

# 과일 개수
fruits = ['사과', '사과', '바나나', '키위']
fruits_dict = defaultdict(int) # 기본값 0
print(fruits_dict)
for f in fruits :
    fruits_dict[f] += 1
print(fruits_dict)
