data = [
    0.00,
    -3.05,
    -4.03,
    -4.51,
    -4.64,
    -4.51,
    -4.15,
    -3.59,
    -2.86,
    -1.99,
    -1.00,
    0.10,
    1.29,
    2.54,
    3.85,
    5.19,
    6.55,
    7.91,
    9.26,
    10.58,
    11.86
]

left = 0
for y in data[:-1]:
    left += y
left = left * 0.1

right = 0
for y in data[1:]:
    right += y
right = right * 0.1

trap = 0
for y in data[1:-1]:
    trap += y
trap = (2 * trap + data[0] + data[-1]) * 0.1 / 2

simpson = 0
coeff = 4
for y in data[1:-1]:
    simpson += coeff * y
    if coeff == 4:
        coeff = 2
    elif coeff == 2:
        coeff = 4
simpson = (simpson + data[0] + data[-1]) * 0.1 / 3


print("\nDifferent Sums:")
print(f"Left: {left:.3f}")
print(f"Right: {right:.3f}")
print(f"Trapezoid: {trap:.3f}")
print(f"Simpson: {simpson:.3f}")

data_derivative_diff = []
for i in range(0, len(data) - 1):
    dy = data[i + 1] - data[i]
    dx = 0.1
    data_derivative_diff.append(dy / dx)

data_derivative_diff2 = []
for i in range(1, len(data) - 1):
    dy = data[i + 1] - data[i - 1]
    dx = 0.2
    data_derivative_diff2.append(dy / dx)



print("\nDerivative lists")
print("First difference:")
[print("{0:0.2f}".format(i), end = " ") for i in data_derivative_diff]
print("\nSecond difference:")
[print("{0:0.2f}".format(i), end = " ") for i in data_derivative_diff2]
print()