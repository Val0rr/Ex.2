import math
a = 0.1
b = 0.9
step = 0.05
print(f"{'x':>6} {'y':>15}")
x = a
while x <= b + 1e-10:
    g = math.cos(2 * x)
    s = math.sin(x) + math.cos(x)
    if abs(g) < 1e-12 or abs(s) < 1e-12:
        y = 'неопределённый'
    else:
        y = (x * math.sin(2 * x)) / g + (x * math.log(x)) / s
    print(f"{x:6.2f} {y if isinstance(y, str) else f'{y:15.6f}'}")
    x+=step
