import unittest
from GraphAlgo import GraphAlgo


class MyTestCase(unittest.TestCase):

    def test_load(self):
        g1 = GraphAlgo()
        g1.load_from_json('../data/500n.json')
        g1.save_to_json('temp.json')
        g1.TSP([4,5,6,8])


        # print(g1.shortest_path(1,70))

def test_save(self):
    g = GraphAlgo()
    g.load_from_json('../data/500n.json')
    g.save_to_json('temp.json')


def test_path(self):
    g = GraphAlgo()
    g.load_from_json('../data/500n.json')
    print(g.shortest_path(8550, 9000))


def test_TSP(self):
    g = GraphAlgo()
    g.load_from_json('../data/500n.json')
    l = [1, 2, 7, 900, 5000]
    print(g.TSP(l))


def test_center(self):
    g = GraphAlgo()
    g.load_from_json('../data/100n.json')
    print(g.centerPoint())
    print(g.isConnected())


if __name__ == '__main__':
    unittest.main()
    g = GraphAlgo()
    g.load_from_json('../data/100n.json')
    print(g.centerPoint())
