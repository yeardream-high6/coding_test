N = int(input())
distances = map(int, input().split())
prices = map(int, input().split())

min_p = 1_000_000_000
cost = 0
for p, d in zip(prices, distances):
    if min_p > p:
        min_p = p
    cost += min_p * d
    
print(cost)