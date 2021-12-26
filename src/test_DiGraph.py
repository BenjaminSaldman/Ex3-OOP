import unittest
from DiGraph import DiGraph
from GraphAlgo import GraphAlgo

class MyTestCase(unittest.TestCase):
    """
    Tester class for DiGraph.
    """
    def test_v_size(self):
        a = GraphAlgo()
        a.load_from_json("A0.json")
        g = a.get_graph()
        self.assertEqual(g.v_size(), 11)
        a.load_from_json("A1.json")
        g = a.get_graph()
        self.assertEqual(g.v_size(), 17)
        a.load_from_json("A2.json")
        g = a.get_graph()
        self.assertEqual(g.v_size(), 31)
        a.load_from_json("A3.json")
        g = a.get_graph()
        self.assertEqual(g.v_size(), 49)
        a.load_from_json("A4.json")
        g = a.get_graph()
        self.assertEqual(g.v_size(), 40)
        a.load_from_json("A5.json")
        g = a.get_graph()
        self.assertEqual(g.v_size(), 48)

    def test_e_size(self):
        a = GraphAlgo()
        a.load_from_json("A0.json")
        g = a.get_graph()
        self.assertEqual(g.e_size(), 22)
        a.load_from_json("A1.json")
        g = a.get_graph()
        self.assertEqual(g.e_size(), 36)
        a.load_from_json("A2.json")
        g = a.get_graph()
        self.assertEqual(g.e_size(), 80)
        a.load_from_json("A3.json")
        g = a.get_graph()
        self.assertEqual(g.e_size(), 136)
        a.load_from_json("A4.json")
        g = a.get_graph()
        self.assertEqual(g.e_size(), 102)
        a.load_from_json("A5.json")
        g = a.get_graph()
        self.assertEqual(g.e_size(), 166)

    def test_get_all_v(self):
        a = GraphAlgo()
        a.load_from_json("A0.json")
        g = a.get_graph()
        d = {0 : (35.18753053591606,32.10378225882353, 0.0), 1 : (35.18958953510896,32.10785303529412, 0.0),
             2 : (35.19341035835351,32.10610841680672, 0.0), 3 : (35.197528356739305,32.1053088, 0.0),
             4 : (35.2016888087167,32.10601755126051, 0.0), 5 : (35.20582803389831,32.10625380168067, 0.0),
             6 : (35.20792948668281,32.10470908739496, 0.0), 7 : (35.20746249717514,32.10254648739496, 0.0),
             8 : (35.20319591121872,32.1031462, 0.0), 9 : (35.19597880064568,32.10154696638656, 0.0),
             10 : (35.18910131880549,32.103618700840336, 0.0)}
        self.assertNotEqual(g.get_all_v().values(), d.values())
        r = g.get_all_v().values()
        q = {}
        for i in r:
            q[i.id] = i.location
        self.assertEqual(q, d)


    def test_all_in_edges_of_node(self):
        a = GraphAlgo()
        a.load_from_json("A0.json")
        g = a.get_graph()
        d = {1: 1.8884659521433524, 10: 1.1761238717867548}
        self.assertEqual(g.all_in_edges_of_node(0), d)

    def test_all_out_edges_of_node(self):
        a = GraphAlgo()
        a.load_from_json("A0.json")
        g = a.get_graph()
        d = {1 : 1.4004465106761335, 10 : 1.4620268165085584}
        self.assertEqual(g.all_out_edges_of_node(0), d)

    def test_get_mc(self):
        a = GraphAlgo()
        a.load_from_json("A0.json")
        g = a.get_graph()
        g.add_node(11, (35.19351649233253,32.1061811092437))
        self.assertEqual(g.get_mc(), 22)

    def test_add_edge(self):
        a = GraphAlgo()
        a.load_from_json("A0.json")
        g = a.get_graph()
        self.assertEqual(g.add_edge(0, 2, 1.4195069847291193), True)
        self.assertEqual(g.add_edge(0, 1, 1.4004465106761335), False)

    def test_add_node(self):
        a = GraphAlgo()
        a.load_from_json("A0.json")
        g = a.get_graph()
        self.assertEqual(g.add_node(11, (35.19351649233253,32.1061811092437)), True)
        self.assertEqual(g.add_node(0, (35.18753053591606,32.10378225882353)), False)

    def test_remove_node(self):
        a = GraphAlgo()
        a.load_from_json("A0.json")
        g = a.get_graph()
        self.assertEqual(g.remove_node(0), True)
        #self.assertEqual(g.remove_node(11), False)

    def test_remove_edge(self):
        a = GraphAlgo()
        a.load_from_json("A0.json")
        g = a.get_graph()
        self.assertEqual(g.remove_edge(0, 1), True)
        self.assertEqual(g.remove_edge(0, 2), False)



def suite():
    suite = unittest.TestSuite()
    suite.addTest('test_v_size')
    suite.addTest('test_e_size')
    suite.addTest('test_get_all_v')
    suite.addTest('test_all_in_edges_of_node')
    suite.addTest('test_all_out_edges_of_node')
    suite.addTest('test_get_mc')
    suite.addTest('test_add_edge')
    suite.addTest('test_add_node')
    suite.addTest('test_remove_node')
    suite.addTest('test_remove_edge')
    return suite

if __name__ == '__main__':
    unittest.main()
