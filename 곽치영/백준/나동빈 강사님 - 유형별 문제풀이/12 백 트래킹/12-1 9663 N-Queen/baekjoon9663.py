n = int(input())

check_queens = [[0] * n for _ in range(n)]

def dfs(i):
    result = 0

    for j in range(n):
        if check_queens[i][j] == 0:
            if i == 0:
                result += 1
            else:
                for k in range(1, i+1):
                    check_queens[i-k][j] += 1
                for k in range(1, min(i+1, j+1)):
                    check_queens[i-k][j-k] += 1
                for k in range(1, min(i+1, n-j)):
                    check_queens[i-k][j+k] += 1

                result += dfs(i-1)

                for k in range(1, i+1):
                    check_queens[i-k][j] -= 1
                for k in range(1, min(i+1, j+1)):
                    check_queens[i-k][j-k] -= 1
                for k in range(1, min(i+1, n-j)):
                    check_queens[i-k][j+k] -= 1
            
    return result

print(dfs(n-1))
