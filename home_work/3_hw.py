def add(x, y):
    return max(x, y)
print(add(181, 226))


a = 135
b = 270

if a - b == 135 or a - b == -135:
    print('yes')
else:
    print('no')


a = 13

if a == 12 or 0 < a < 4:
    print('зима')
elif 3 <= a < 6:
    print('весна')
elif 6 <= a <= 8:
    print('лето')
elif 9 <= a <=12:
    print('осень')
else:
    print('неверный месяц')


w = 11
e = 11
r = 11

if w > 10 and e > 10 and r > 10:
    print('yes')
else:
    print('no')


z = 1
x = 2
c = -3
v = -4
b = -5

summ = 0
sub = 0

if z > 0:
    summ = summ + 1
else:
    sub = sub + 1
if x > 0:
    summ = summ + 1
else:
    sub = sub + 1
if c > 0:
    summ = summ + 1
else:
    sub = sub + 1
if v > 0:
    summ = summ + 1
else:
    sub = sub + 1
if b > 0:
    summ = summ + 1
else:
    sub = sub + 1
    print(summ)
    #






