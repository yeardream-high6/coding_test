price = int(input())
coins = [500, 100, 50, 10, 5, 1]
coin_cnt = 0
remainder = 1000 - price
for coin_value in coins:
    num_coin = remainder // coin_value
    remainder -= coin_value * num_coin
    coin_cnt += num_coin
print(coin_cnt)
