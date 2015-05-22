import unittest
import graph_tools


class TestGraphTools(unittest.TestCase):

    def setUp(self):
        self.g = {
            'A': ['B', 'C'],
            'C': ['B'],
            'D': ['C', 'E'],
            'K': []
        }

    def assertEq(self, actual, expected):
        try:
            self.assertTrue(all(x == y for x, y in zip(actual, expected)))
        except AssertionError:
            raise AssertionError('%s is not %s' % (actual, expected))

    def test_reverse_graph(self):
        rg = graph_tools.reverse_graph(self.g)

        children_a = rg['A']
        self.assertTrue(len(children_a) == 0)

        children_b = rg['B']
        self.assertTrue('A' in children_b)
        self.assertTrue('C' in children_b)

        children_c = rg['C']
        self.assertTrue('A' in children_c)
        self.assertTrue('D' in children_c)

        self.assertTrue('K' in rg)

    def test_sinks(self):
        sinks = graph_tools.sinks(self.g)

        self.assertTrue('B' in sinks)
        self.assertTrue('K' in sinks)
        self.assertTrue('E' in sinks)

    def test_topsort(self):
        topsort = graph_tools.topsort(self.g)
        self.assertEq(topsort, ['K', 'D', 'A', 'E', 'C', 'B'])

if __name__ == '__main__':
    unittest.main()
