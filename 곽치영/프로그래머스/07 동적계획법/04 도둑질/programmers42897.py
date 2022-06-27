def solution(money):
    money = iter(money)
    dp, dp_no_last = next(money), 0
    dp_no_first, dp_no_first_no_last = 0, 0
    for m in money:
        dp, dp_no_last = max(m + dp_no_last, dp), dp
        dp_no_first, dp_no_first_no_last = max(m + dp_no_first_no_last, dp_no_first), dp_no_first
    return max(dp_no_first, dp_no_last)