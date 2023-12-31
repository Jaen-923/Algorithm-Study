# 순차 탐색 : 리스트 안에 있는 특정한 데이터를 찾기 위해 앞에서부터 데이터를 하나씩 차례대로 확인하는 방법
# 리스트 내에 데이터가 아무리 많아도 시간만 충분하다면 항상 원하는 데이터를 찾을 수 있다.
# 데이터 정렬 여부와 상관없이 가장 앞에 있는 원소부터 하나씩 확인해야 한다.
# 최악의 경우 시간 복잡도는 O(N)

def sequential_search(n, target, array):
    for i in range(n):
        if array[i] == target:
            return i+1 # 인덱스는 0부터 시작하므로

print("생성할 원소 개수를 입력한 다음 한 칸 띄고 찾을 문자열을 입력하세요.")
input_data = input().split()
n = int(input_data[0]) # 원소 개수
target = input_data[1] # 찾고자 하는 문자열

print("앞서 적은 원소 개수 만큼 문자열을 입력하세요. 구분은 띄어쓰기 한 칸으로 합니다.")
array = input().split()

print(sequential_search(n, target, array))

