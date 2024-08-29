# %%

# 제너레이터(generator)
# 제너레이터 객체를 호출할 때마다 yield까지 문장을 실행하고 멈춤

# 예시
def generator_func():
    print('1번 항목 처리')
    yield 1
    print('2번 항목 처리')
    yield 2
    print('3번 항목 처리')
    yield 3

g = generator_func()
print(g)
print(next(g))
print(next(g))
print(next(g))
# print(next(g)) # 반환할 것이 없어서 error

# 제너레이터 객체를 다시 처음부터 사용하고 싶은 경우에는 재할당
g = generator_func()
for i in g:
    print('i', i)

# %%

# 제너레이터 사용 이유
# - 제너레이터로 반복 가능한 객체를 만들지 않으면 선언과 동시에 메모리 소요
# - 데이터 양이 많은 겨우 아래와 같은 코드는 메모리 효율성이 좋지 않음

nums = [i for i in range(int(1e6))]
print(nums)

# - 제너레이터를 통해 반복 가능한 객체를 생성하고 호출하면 다음 순서를 기억함
# - 호출하기 전에는 모든 값을 메모리에 할당하지 않음 (지연 평가 방식)

# 튜플이 아니라 제너레이터 컴프리헨션
nums = (i for i in range(int(1e6)))
print(nums) # 숫자가 메모리에 할당되지 않은 상태
for i in nums:
    print(i, end=',') # 호출될 때마다 하나씩 메모리에 할당

# 제너레이터 사용 이유
# - 대용량 데이터 처리에 사용
# - 지연평가로 인해 특정 조건을 만족하는 값을 찾는 경우
# - 무한 시퀀스를 만들 경우 사용

# 무조건 제너레이터를 사용해야 하는지??
# - 작은 크기의 데이터나 한 번에 모든 값을 필요로 하는 경우에는 리스트를 사용하는 것이 좋음

# %%

# 무한 시퀀스 예제
# - 피보나치 수열
# - 1 1 2 3 5 8 13 21 ...
# - fibo(n) = fibo(n-1) + fibo(n-2)
def fibo_generator():
    n1, n2 = 1, 1
    while True:
        yield n1
        n1, n2 = n2, n1+n2

fibo_g = fibo_generator()
for i in range(10):
    print(next(fibo_g))

# %%

# 조건 함수
# all
# - 반복 가능한 자료형의 모든 요소가 참이면 참 반환
# - 하나라도 거짓이면 거짓 반환
# - 인자로 받은 요소가 비어있으면 참 반환
print(all([1,2,3,'Hello'])) # True
print(all([1,2,3,''])) # False
print(all([])) # True
print(all([i for i in range(10)])) # False # 리스트 컴프리헨션
print(all(i for i in range(10))) # False # 제너레이터 컴프리헨션

# any
# - 반복 가능한 자료형의 요소가 하나라도 참이면 참을 반환
# - 모든 요소가 거짓이면 거짓 반환
# - 인자로 받은 요소가 비어 있으면 거짓 반환
print(any([0,0,0,'Hello'])) # True
print(any([0,0,0,''])) # False
print(any([])) # False
print(any(i for i in range(3))) # True # 제너레이터 컴프리헨션

# %%

# for-else와 while-else 구문
# - 반복문이 정상적으로 완료되었을 때 실행하는 코드 블록 정의
# - 반복문이 break, 에러 등으로 중단되지 않고 정상적으로 모든 요소를 순회하거나 반복 조건이 False가 되었을 때 else 구문 실행

for elem in iterable:
    if break_cond:
        # 특정 조건 하에 반복문 종료
        break
else:
    # 정상적으로 완료된 경우에 실행될 코드
    ...

while cond:
    if break_cond:
        # 특정 조건 하에 반복문 종료
        break
else:
    # 정상적으로 완료된 경우에 실행될 코드
    ...

# %%

# for-else 예시
def find_number(numbers, target):
    for i, num in enumerate(numbers):
        if num == target:
            print(f'인덱스 {i}에서 {target}을 찾았습니다.')
            break
    else:
        print(f'{target}을 찾지 못했습니다.')

nums = [1,2,3,4]
find_number(nums,3)
find_number(nums,7)
find_number([],3)

# %%

# while-else 예시
def find_number(numbers, target):
    i = 0
    while i < len(numbers):
        num = numbers[i]
        if num == target:
            print(f'인덱스 {i}에서 {target}을 찾았습니다.')
            break
        i += 1
    else:
        print(f'{target}을 찾지 못했습니다.')

nums = [1,2,3,4]
find_number(nums,3)
find_number(nums,7)
find_number([],3)
