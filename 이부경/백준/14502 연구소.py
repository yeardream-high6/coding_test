# PyPy3로 제출 시에 통과합니다.
def spread_virus(arr):
    def spread(arr, i, j, start=False):
        if i < 0 or i >= M or j < 0 or j >= N:
            return
        
        if arr[i][j] == 0 or start:
            arr[i][j] = 2
            spread(arr, i-1, j)
            spread(arr, i+1, j)
            spread(arr, i, j-1)
            spread(arr, i, j+1)
    
    for i in range(M):
        for j in range(N):
            if arr[i][j] == 2:
                spread(arr, i, j, True)
    return arr

def count_safe_area(arr):
    count = 0
    for i in range(M):
        for j in range(N):
            if arr[i][j] == 0:
                count += 1
    return count

def copy_arr(arr1):
    arr2 = []
    for i in range(M):
        arr2.append(arr1[i][:])
    return arr2

def f(arr, n):
    global max_safe_area
    if n == 3:
        contaminated_arr = spread_virus(copy_arr(arr))
        safe_area = count_safe_area(contaminated_arr)
        if max_safe_area < safe_area:
            max_safe_area = safe_area
        return 
    
    for i in range(M):
        for j in range(N):
            if arr[i][j] == 0:
                arr[i][j] = 1
                f(arr, n + 1)
                arr[i][j] = 0


M, N = map(int, input().split())
arr = []
for _ in range(M):
    arr.append(list(map(int, input().split())))
max_safe_area = 0
f(arr, 0)
print(max_safe_area)