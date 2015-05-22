from inject import injected
import random


def a():
    print 'A'
    return 'A %s' % round((random.random()), 2)


def b(a):
    print 'B (%s)' % a
    return 'B'


def c(a, b):
    print 'C (%s %s)' % (a, b)
    return 'C'


def d(b, c, a):
    print 'D (%s %s %s)' % (a, b, c)
    return 'D'


if __name__ == '__main__':
    G = dict(a=a, b=b, c=c, d=d)

    a = injected(a, namespace=G)
    b = injected(b, namespace=G)
    c = injected(c, namespace=G)
    d = injected(d, namespace=G)

    print a(), '\n'
    print b(), '\n'
    print c(), '\n'
    print d(), '\n'
    print d()
