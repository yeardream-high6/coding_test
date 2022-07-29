# a = fixed cost, b = variable cost, c = sales price
# To calculate break-even point in units use the formula : a * i > b + (c * i) where i refers to the number of production

 
a, b, c = map(int,input().split(' '))

if c <= b:
    print(-1)
else:
    print(a//(c-b)+1)