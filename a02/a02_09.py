def ret(x,y):
    return x*1 + y*1 - 10

ret(3,4)
a,b = 3,4

for i in range(1, 10):
    r = ret(a,b)
    print('a:{}, b:{}, r:{}'.format(a, b, r))
    if r > 0:
        print(i)
        break
    a, b = a + (a * 0.1), b + (b * 0.1)