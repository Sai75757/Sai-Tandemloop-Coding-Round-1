# Sai-Tandemloop-Coding-Round-1
# Python
def generate_series(x):
    series = []
    for i in range(1, x+1):
        series.append(2*i - 1)
    return series

# Example
x = int(input("Enter a number:"))
series = generate_series(x)
print(series)
