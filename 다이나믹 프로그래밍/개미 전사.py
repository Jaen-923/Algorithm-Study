# 개미 전사 : 개미 전사를 위해 식량창고 N개에 대한 정보가 주어졌을 때 얻을 수 있는 식량의 최댓값을 구하는 프로그램
# 단 최소한 한 칸 이상 떨어진 식량창고를 약탈해야 한다.

# 입력 조건
# 첫째 줄에 식량창고의 개수 N이 주어진다. (3<=N<=100)
# 둘째 줄에 공백으로 구분되어 각 식량창고에 저장되 식량의 개수 K가 주어진다. (0<=K<=1000)

# 출력 조건
# 첫쨰 줄에 개미 전사가 얻을 수 있는 식량의 최댓값을 출력하시오.

# 보텀업 방식의 풀이

N = int(input())
array = list(map(int, input().split()))

# 앞서 계산된 결과를 저장하기 위한 DP 테이블 초기화
d = [0]*100

d[0] = array[0]
d[1] = max(array[0], array[1])
for i in range(2, N):
    d[i] = max(d[i-1], d[i-2] + array[i])

print(d[N-1])
