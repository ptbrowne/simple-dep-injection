import unittest
import graph_tools


class TestGraphTools(unittest.TestCase):

    def setUp(self):
        self.g = {
            'A': ['B', 'C'],
            'B': [],
            'C': ['B'],
            'D': ['C', 'E'],
            'K': [],
            'E': []
        }

    def test_reverse_graph(self):
        rg = graph_tools.reverse_graph(self.g)

        children_a = rg['A']
        self.assertEqual(len(children_a), 0)

        children_b = rg['B']
        self.assertIn('A', children_b)
        self.assertIn('C', children_b)

        children_c = rg['C']
        self.assertIn('A', children_c)
        self.assertIn('D', children_c)

        self.assertIn('K', rg)

    def test_sinks(self):
        sinks = graph_tools.sinks(self.g)

        self.assertIn('B', sinks)
        self.assertIn('K', sinks)
        self.assertIn('E', sinks)

    def test_topsort(self):
        self.assertEqual(
            list(graph_tools.topsort(self.g)),
            ['K', 'D', 'A', 'E', 'C', 'B'])

if __name__ == '__main__':
    unittest.main()
