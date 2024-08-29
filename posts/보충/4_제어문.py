# %%

# 조건문
# 봄, 여름, 가을, 겨울
month = 7
if 3 <= month <= 5 :
    season = '봄'
elif 6 <= month <= 8 :
    season = '여름'
elif 9 <= month <= 11 :
    season = '가을'
else :
    season = '겨울'  # month in [1,2,12]
print(f'{month}월의 계절은 {season}입니다.')

# 특정 범위의 값을 미리 정의된 카테고리로 매핑할 때 조건문을 대체할 수 있음
# 코드도 간결해지고 실행속도도 빠름
season = ['겨울']*2 + ['봄']*3 + ['여름']*3 + ['가을']*3 + ['겨울']
print(f'{month}월의 계절은 {season[month-1]}입니다.')

# %%

# 학점
# 90점 이상 : A
# 80점 이상 : B
# 70점 이상 : C
# 60점 이상 : D
# 50점 이상 : F
score = 49
check = ['F','D','C','B','A']
print(f'{score} 점수는 학점 {check[min(4, max(0, score//10 - 5))]}입니다.')
print(f'{score} 점수는 학점 {check[min(4, max(0, int((score-50.000000001)//10)))]}입니다.') # 얘는 초과 구현

# %%

# 습도
# 0~25% 미만 : 건조
# 25~50% 미만 : 적정
# 50~75% 미만 : 습함 
# 75% 이상 : 매우 습함
humidity_levels = ['건조', '적정', '습함', '매우 습함']
humidity = 65
level_index = min(humidity//25, len(humidity_levels)-1)
print(f'습도 {humidity}%의 수준 : {humidity_levels[level_index]}')

# %%

# 혈압
# 90 미만 : 저혈압
# 90-110 미만 : 정상
# 110-130 미만 : 주의
# 130-150 미만 : 높음
# 150 이상 : 위험
categories = ['저혈압', '정상', '주의', '높음', '위험']
bp = 120
categories_index = min(max(0,(bp-70))//20, len(categories)-1)
print(f'혈압 {bp} 수준 : {categories[categories_index]}')

# %%

# 00:00:00 ~ 23:59:59 초 사이에 7이 몇번 출력되는지 개수를 구하시오.
count = 0
for h in range(24):
    for m in range(60):
        for s in range(60):
            time = f'{h}:{m}:{s}'
            count += time.count('7')

print(count)

def count_sevens(hour=0, min=0, sec=0) :
    time = f"{hour}:{min}:{sec}"
    cnt = time.count('7')
    sec += 1
    if sec >= 60 :
        sec = 0
        min += 1
        if min >= 60 :
            min = 0
            hour += 1
    
    if hour < 24 :
        return cnt + count_sevens(hour, min, sec)
    else :
        return cnt

print(count_sevens())

# 재귀함수의 최대 호출 횟수 지정
import sys
sys.setrecursionlimit(10000)

# %%

# 삼항 연산자 조건문
# 변수 = 참값 if 조건식 else 거짓인 경우 값
num = 5
num_type = '짝수' if num%2==0 else '홀수'

nums = list(range(10))
nums = ['짝수' if n%2==0 else '홀수' for n in nums]
print(nums)

nums = list(range(10))
nums = [(n, '짝수') for n in nums if n%2==0]
print(nums)
