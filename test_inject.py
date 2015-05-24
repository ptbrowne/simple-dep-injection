import unittest
from inject import get_deps, call, injected

def a(b,c,d): return ''.join(['A', b, c, d])
def b(c, d): return ''.join(['B', c, d])
def c(d): return ''.join(['C', d])
def d(): return ''.join(['D'])


class DepInjectTest(unittest.TestCase):
    def setUp(self):
        self.ns = dict(a=a, b=b, c=c, d=d)

    def test_get_deps(self):
        deps = get_deps(self.ns['a'], namespace=self.ns)

        self.assertEqual(set(['b', 'c', 'd']), set(deps['a']))
        self.assertEqual(set(['c', 'd']), set(deps['b']))
        self.assertEqual(set(['d']), set(deps['c']))
        self.assertEqual(set(), set(deps['d']))

    def test_execute_with_deps(self):
        res = call(self.ns['a'], namespace=self.ns)
        self.assertEqual(res, 'ABCDDCDD')

    def test_injected(self):
        inj = injected(self.ns['a'], namespace=self.ns)
        res = inj()
        self.assertEqual(res, 'ABCDDCDD')

if __name__ == '__main__':
    unittest.main()
