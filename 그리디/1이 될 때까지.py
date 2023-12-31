# 1이 될 때까지 : 어떠한 수 N이 1이 될 때까지 아래의 두 과정 중 하나를 반복적으로 선택하여 수행
# 1. N에서 1을 뺀다.
# 2. N을 K로 나눈다. (단 N이 K로 나누어 떨어질 때만 선택할 수 있다.)

# 입력 조건
# 첫째 줄에 N(2<=N<=100000)과 K(2<=K<=100000)가 공백으로 구분되며 각각 자연수로 주어진다. 이때 입력으로 주어지는 N은 항상 K보다 크거나 같다.

# 출력 조건
# 첫째 줄에 N이 1이 될 때까지 1번 혹은 2번의 과정을 수행해야 하는 횟수의 최솟값을 출력한다.

import timeit

start_time = timeit.default_timer()

N, K = map(int, input().split())
cnt = 0

while N != 1:
    if N % K == 0:
        N /= K
        cnt += 1
        continue
    N -= 1
    cnt += 1

print(cnt)

end_time = timeit.default_timer()
execution_time = end_time - start_time

print(f"Execution Time: {execution_time} seconds")


