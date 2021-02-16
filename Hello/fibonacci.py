series = [0, 1, 1]
a = 1
b = 1
for i un range(1,9):
    c = b+a
    series.append(c)
    a=b
    b=c
print(series)