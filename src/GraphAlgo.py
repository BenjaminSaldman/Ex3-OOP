import math

from src.GraphAlgoInterface import GraphAlgoInterface
from src.GraphInterface import GraphInterface
from src.DiGraph import DiGraph
import json
from queue import PriorityQueue
from Node import Node


class GraphAlgo(GraphAlgoInterface):
    def __init__(self, g: GraphInterface = DiGraph()):
        self.g = g

    def get_graph(self) -> GraphInterface:
        """
        :return: the directed graph on which the algorithm works on.
        """
        return self.g

    def load_from_json(self, file_name: str) -> bool:
        g = DiGraph()
        try:
            with open(file_name, "r") as f:
                d = json.load(f)
        except IOError as e:
            print(e)
            return False
        for i in d["Nodes"]:
            if "pos" not in i.keys():
                g.add_node(i["id"])
            else:
                temp = i["pos"].split(",")
                p = (float(temp[0]), float(temp[1]), float(temp[2]))
                g.add_node(i["id"], p)
        for j in d["Edges"]:
            src = j["src"]
            w = j["w"]
            dest = j["dest"]
            g.add_edge(src, dest, w)
        self.g = g
        return True;

    def save_to_json(self, file_name: str) -> bool:
        """
        Saves the graph in JSON format to a file
        @param file_name: The path to the out file
        @return: True if the save was successful, False o.w.
        """
        try:
            with open(file_name, "w") as f:
                g = {}
                Nodes = []
                Edges = []

                for i in self.g.get_all_v().values():
                    if i.location is None:
                        Nodes.append({"id": i.id})
                    else:
                        Nodes.append(
                            {"id": i.id,
                             "pos": str(i.location[0]) + "," + str(i.location[1]) + "," + str(i.location[2])})
                    for j, k in self.g.all_out_edges_of_node(i.id).items():
                        Edges.append({"src": i.id, "w": k, "dest": j})
                g["Edges"] = Edges
                g["Nodes"] = Nodes
                json.dump(g, fp=f, indent=6)
                return True

        except IOError as e:
            print(e)
            return False

    def initGraph(self) -> None:
        for i in self.g.Nodes.values():
            i.tag = 0
            i.weight = math.inf

    def getNode(self, id1: int):
        return self.g.Nodes[id1]

    def Dijkstra(self, start: Node):
        self.initGraph()
        q = PriorityQueue()
        start.weight = 0
        q.put(start)
        while not q.empty():
            node = q.get()
            ed = self.g.all_out_edges_of_node(node.id)
            for i, j in ed.items():
                neighbor = self.getNode(i)
                alt = node.weight + j
                if neighbor.weight > alt:
                    neighbor.weight = alt
                    neighbor.tag = node.id
                    q.put(neighbor)


    def shortest_path(self, id1: int, id2: int) -> (float, list):
        if id1 not in self.g.get_all_v() and id2 not in self.g.get_all_v():
            return (math.inf, [])
        self.initGraph()
        self.Dijkstra(self.getNode(id1))
        dist = self.getNode(id2).weight
        path = []
        rev = self.getNode(id2)
        while rev != self.getNode(id1):
            path.append(rev.id)
            rev = self.getNode(rev.tag)
        path.append(id1)
        path.reverse()
        p = (dist, path)
        if dist >= math.inf:
            p = (math.inf, [])
        return p


    def centerPoint(self) -> (int, float):

        min = math.inf
        ans = 0
        currMax = 0
        for i in self.g.Nodes.values():
            for j in self.g.Nodes.values():
                ave = self.shortest_path(i.id, j.id)[0]
                if ave > currMax:
                    currMax = ave
            if currMax < min:
                min = currMax
                ans = i.id
            currMax = 0
        print(ans)
        print(min)
        p = (ans, min)
        return p
