from numpy import e
from numpy import log

f = lambda x,y : 4*x + 5*y - 9

sigma = lambda x,y: 1 / (1 + e**(-1 * f(x,y)))
softmax = lambda x, y: (e ** x) / ((e**x) + (e**y))

def cross_entropy(ylist, plist):
    result = []
    for p, y in zip(plist, ylist):
        ce = y * log(p) + (1 - y) * log(1 - p)
        result.append(ce)
    return result

sigma(10,1)
softmax(1,5)


 # w1*0.4 + w2*0.6 + b.
fx = lambda a, b, c: a*0.4 + b*0.6 + c
perc = lambda a,b,c: 1 / (1 + e**(-1 * fx(a,b,c)))

perc(1,2,3)
perc(2,6,-2)
perc(3,5,-2.2)
perc(5,4,-3)

perc(1,1,0)
perc(10,10,0)