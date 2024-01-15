def max_profit(A):
    if not A or len(A) < 2:
        return 0

    max_profit = 0
    min_price = A[0]

    for price in A[1:]:
        max_profit = max(max_profit, price - min_price)
        min_price = min(min_price, price)

    return max_profit


input_1 =[]
a = int(input())
for i in range(a):
    j = int(input())
    input_1.append(j)

output = max_profit(input_1) 

print(output)
