import unittest
from DiGraph import DiGraph
from GraphAlgo import GraphAlgo
from Node import Node

class MyTestCase(unittest.TestCase):
    """
    Tester class for GraphAlgo.
    """
    def test_get_graph(self):
        a = GraphAlgo()
        a.load_from_json("A0.json")
        a1 = GraphAlgo()
        a1.load_from_json("A1.json")
        self.assertNotEqual(a.get_graph(), a1.get_graph())

    def test_load_from_json(self):
        a = GraphAlgo()
        a.load_from_json("A0.json")
        a0 = GraphAlgo()
        a0.load_from_json("A0.json")
        a1 = GraphAlgo()
        a1.load_from_json("A1.json")
        self.assertNotEqual(a, a0)
        self.assertNotEqual(a, a1)

    def test_save_to_json(self):
        a = GraphAlgo()
        a.load_from_json("A0.json")
        a.save_to_json("testing.json")
        g = a.get_graph()
        a.load_from_json("testing.json")
        g1 = a.get_graph()
        self.assertEqual(g.Nodes, g1.Nodes)
        self.assertEqual(g.Edges, g1.Edges)


    def test_initGraph(self):
        a = GraphAlgo()
        a.load_from_json("A0.json")
        a1 = GraphAlgo()
        a.load_from_json("A1.json")
        self.assertEqual(a.initGraph(a.get_graph()), a1.initGraph(a1.get_graph()))

    def test_centerPoint(self):
        a = GraphAlgo()
        a.load_from_json("A0.json")
        self.assertEqual(a.centerPoint(), (7, 6.806805834715163))
        a.load_from_json("A1.json")
        self.assertEqual(a.centerPoint(), (8, 9.925289024973141))
        a.load_from_json("A2.json")
        self.assertEqual(a.centerPoint(), (0, 7.819910602212574))
        a.load_from_json("A3.json")
        self.assertEqual(a.centerPoint(), (2, 8.182236568942237))
        a.load_from_json("A4.json")
        self.assertEqual(a.centerPoint(), (6, 8.071366078651435))
        a.load_from_json("A5.json")
        self.assertEqual(a.centerPoint(), (40, 9.291743173960954))

    def test_isConnected(self):
        a = GraphAlgo()
        a.load_from_json("A0.json")
        self.assertEqual(a.isConnected(), True)
        a = GraphAlgo()
        a.load_from_json("A1.json")
        self.assertEqual(a.isConnected(), True)
        a = GraphAlgo()
        a.load_from_json("A2.json")
        self.assertEqual(a.isConnected(), True)
        a = GraphAlgo()
        a.load_from_json("A3.json")
        self.assertEqual(a.isConnected(), True)
        a = GraphAlgo()
        a.load_from_json("A4.json")
        self.assertEqual(a.isConnected(), True)
        a = GraphAlgo()
        a.load_from_json("A5.json")
        self.assertEqual(a.isConnected(), True)

    def test_TSP(self):
        a = GraphAlgo()
        a.load_from_json("A0.json")
        l = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        w = 1.4004465106761335 + 1.7646903245689283 + 1.1435447583365383 + 1.4301580756736283 + 1.9442789961315767 \
            + 1.160662656360925 + 1.3968360163668776 + 1.354895648936991 + 1.8526880332753517 + 1.022651770039933
        g = a.get_graph()
        d = list(g.get_all_v())
        self.assertEqual(a.TSP(d), (l, w))

    def test_shortest_path(self):
        a = GraphAlgo()
        a.load_from_json("A0.json")
        correct = [0, 1]
        wrong = [0, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
        correctW = 1.4004465106761335
        wrongW = 1.4620268165085584 + 1.0887225789883779 + 1.4575484853801393 + 1.354895648936991 + 1.3968360163668776 \
                 + 1.160662656360925 + 1.9442789961315767 + 1.4301580756736283 + 1.1435447583365383 + 1.7646903245689283
        self.assertEqual(a.shortest_path(0, 1), (correctW, correct))
        self.assertNotEqual(a.shortest_path(0, 1), (wrongW, wrong))


if __name__ == '__main__':
    unittest.main()
