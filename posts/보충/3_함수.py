# %%

# 독스트링 호출
print(help(int))

# 사용 가능한 메서드 및 변수 목록
print(dir(list))

# %%

# 타입 체크
print(isinstance(10, int))
print(isinstance(10, float))

# %%

# 재귀함수
# 예시 1) 리스트의 요소를 모두 더하는 함수
# 방법 1
def sum_list(nums):
    if not nums:
        return 0
    else :
        return nums[0] + sum_list(nums[1:])
    
nums = [1,2,3,4,5]
sum_list(nums)

# %%

# 슬라이싱을 안해도 돼서 효율적
# idx를 바꿀 수 있으니 더 많은 경우에 사용 가능
# 방법 2
def sum_list(nums, idx):
    if len(nums) <= idx:  # ==도 되는데 >=이 좀 더 안정적
        return 0
    else :
        return nums[idx] + sum_list(nums, idx+1)

nums = [1,2,3,4,5]
sum_list(nums, 0)

# %%

# 예시 2) 문자열 뒤집어서 출력
# 함수 또는 알고리즘 설계
# 입력 : 문자열
# 출력 : 문자열
# 문제풀이 (재귀함수 이용)
### 문자열 더하기 이용
### recur(다음 문자 인덱스) + 현재 문자
### 종료 조건 : 인덱스가 문자열 길이보다 같거나 클 때 종료

# 방법 1 (강사님 코드)
def reverse_sort(text, idx):
    if idx >= len(text):
        return ''
    else :
        return reverse_sort(text, idx+1) + text[idx]
    
text = 'hello'
reverse_sort(text, 0)

# %%

# 방법 2 (내 코드)
def reverse_sort(text, idx):
    if not idx :
        return text[0]
    else :
        return text[idx] + reverse_sort(text, idx-1)
    
text = 'hello'
reverse_sort(text, len(text)-1)

# %%

# 람다 활용
radius = [1,2,5,10]
print(sorted(radius))
print(sorted(radius, reverse=True))

# 원의 넓이 순으로 정렬
print(sorted(radius, key=lambda r:3.14*r**2))

# 사각형
rects = [(1,2), (3,3), (1,1), (10,9)]  # (가로,세로)
print(sorted(rects))  # 가로 길이 순으로
print(sorted(rects, key=lambda rect: rect[1]))  # 세로 길이 순으로
print(sorted(rects, key=lambda rect: rect[0]*rect[1]))  # 넓이 순으로

# 정렬 조건 세분화
# 정렬 값이 동일한 경우 그 다음 정렬 조건으로 정렬
# ex ) 가로 길이 오름차순 - 세로 길이 내림차순
print(sorted(rects, key=lambda rect: (rect[0], -rect[1])))

# %%

# map은 iterable(리스트)한 객체를 통해 새로운 iterable(리스트)를 만들 때 사용
names = ['홍길동', '임꺽정', '김현수']
ages = [20, 30, 35]
n = 0

# 딕셔너리 형태로 바꿔서 리스트로 저장
def create_user(name, age) :
    global n
    n += 1
    return {'번호': n, '이름': name, '나이': age}
members = list(map(create_user, names, ages))
print(members)

# %%

# filter
print(list(filter(lambda m: m['나이'] > 20, members)))

# 원의 넓이가 10이상인 반지름
radius = [1,2,5,10]
print(list(filter(lambda r: 3.14*r**2 > 10, radius)))
