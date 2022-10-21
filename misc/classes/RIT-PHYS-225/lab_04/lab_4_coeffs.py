import numpy


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

print()


mat = []

dx = 0.1
for i in range(0, len(data)):
    temp = []
    for k in range(0, len(data)):
        temp.append((i * dx) ** k)
    mat.append(temp)

mat = numpy.asarray(mat)
y_output = numpy.asarray(data)
inv_mat = numpy.linalg.inv(mat)

coeffs = numpy.matmul(inv_mat, y_output)




def evaluate(x):
    y = 0
    for i in range(0, len(data)):
        y += coeffs[i] * (x ** i)
    print(y)


for i in range(0, len(data)):
    evaluate(0.1 * i)
