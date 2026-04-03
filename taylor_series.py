x = 1.0
result = 0
for i in range(5):
    term = x**(2*i + 1) / factorial(2*i + 1)
if i % 2 == 0:
    result += term
else:
    result -= term