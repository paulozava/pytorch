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

sigma(1,5)
softmax(1,5)