from numpy import e

f = lambda x,y : 4*x + 5*y - 9

sigma = lambda x,y: 1 / (1 + e**(-1 * f(x,y)))
softmax = lambda x, y: (e ** x) / ((e**x) + (e**y))

sigma(1,5)
softmax(1,5)


