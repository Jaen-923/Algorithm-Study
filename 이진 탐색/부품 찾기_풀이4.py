# 집합 자료형을 이용한 풀이 -> set() 함수
# 집합 자료형은 단순히 특정한 데이터가 존재하는지 검사할 때에 매우 효과적으로 사용할 수 있다.

N = int(input())
array = set(map(int, input().split()))

M = int(input())
X = list(map(int, input().split()))

for i in X:
    if i in array:
        print('yes', end=' ')
    else:
        print('no', end=' ')
