import math
from src.GraphAlgoInterface import GraphAlgoInterface
from src.GraphInterface import GraphInterface
from src.DiGraph import DiGraph
import json
from queue import PriorityQueue
from Node import Node
import matplotlib.pyplot as plt
from queue import Queue


class GraphAlgo(GraphAlgoInterface):
    def __init__(self, g: GraphInterface = DiGraph()):
        self.g = g

    def get_graph(self) -> GraphInterface:
        """
        :return: the directed graph on which the algorithm works on.
        """
        return self.g

    def load_from_json(self, file_name: str) -> bool:
        """

        :param file_name:
        :return: true if the load succeed, else return false.
        """
        g = DiGraph()  # create new graph.
        try:
            with open(file_name, "r") as f:  # Opening the file.
                d = json.load(f)  # d contains the json object.
        except IOError as e:
            print(e)
            return False
        for i in d["Nodes"]:  # Extract the nodes from the object.
            if "pos" not in i.keys():  # Check case for T0 , if the nodes doesn't have location just add the id.
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
                """
                Adding the nodes and the edges to Nodes[] and Edges[].
                """
                for i in self.g.get_all_v().values():
                    if i.location is None:
                        Nodes.append({"id": i.id})
                    else:
                        Nodes.append(
                            {
                                "pos": str(i.location[0]) + "," + str(i.location[1]) + "," + str(i.location[2]),
                                "id": i.id})
                    for j, k in self.g.all_out_edges_of_node(i.id).items():
                        Edges.append({"src": i.id, "w": k, "dest": j})
                g["Edges"] = Edges
                g["Nodes"] = Nodes
                # Creating the json file.
                json.dump(g, fp=f, indent=6)
                return True

        except IOError as e:
            print(e)
            return False

    def initGraph(self, graph: DiGraph) -> None:
        for i in graph.Nodes.values():
            i.tag = 0
            i.weight = math.inf

    def getNode(self, id1: int):
        return self.g.Nodes[id1]

    def Dijkstra(self, start: Node):
        self.initGraph(self.g)
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
        self.initGraph(self.g)
        self.Dijkstra(self.getNode(id1))
        dist = self.getNode(id2).weight
        if dist == math.inf:
            return (math.inf, [])
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

        p = (ans, min)
        return p

    def plot_graph(self) -> None:
        """
        Plots the graph.
        If the nodes have a position, the nodes will be placed there.
        Otherwise, they will be placed in a random but elegant manner.
        @return: None
        """
        for i in self.g.get_all_v().values():
            x = y = z = 0
            if i.location is None:
                x = (i.id + 20) * (i.id + 20) + 20
                y = i.id * i.id * i.id
            else:
                p = i.location
                x = p[0]
                y = p[1]
                z = p[2]
            plt.plot(x, y, markersize=10, marker=".", color="red")
            plt.text(x, y, str(i.id), color="green", fontsize=12)
            for k in self.g.all_out_edges_of_node(i.id).items():
                n = self.getNode(k[0])
                dx = dy = 0
                if n.location is None:
                    dx = (n.id + 20) * (n.id + 20) + 20
                    dy = n.id * n.id * n.id
                else:
                    p = n.location
                    dx = p[0]
                    dy = p[1]

                plt.annotate("", xy=(x, y), xytext=(dx, dy), arrowprops=dict(arrowstyle="<-"))
        plt.show()

    def transpose(self) -> DiGraph:
        tr = DiGraph()
        for i in self.g.Nodes.values():
            tr.add_node(i.id, i.location)
        for i in self.g.Nodes.values():
            for j, k in self.g.all_out_edges_of_node(i.id).items():
                tr.add_edge(j, i.id, k)
        return tr

    def BFS(self, start: int, graph: DiGraph) -> None:
        q = Queue()
        n = graph.Nodes.get(start)
        q.put(n)
        n.tag = 1
        while not q.empty():
            n = q.get()
            for i in graph.all_out_edges_of_node(n.id):
                if graph.Nodes[i].tag != 1:
                    graph.Nodes[i].tag = 1
                    q.put(graph.Nodes[i])

    def isConnected(self) -> bool:
        if self.g is None:
            return True
        if len(self.g.get_all_v()) <= 1:
            return True
        if len(self.g.get_all_v()) > self.g.e_size() + 1:
            return False
        tr = self.transpose()
        self.initGraph(self.g)
        self.initGraph(tr)
        self.BFS(0, self.g)
        self.BFS(0, tr)
        for i in self.g.Nodes.values():
            if i.tag != 1:
                return False
        for i in tr.Nodes.values():
            if i.tag != 1:
                return False
        return True

    def TSP(self, node_lst: list[int]) -> (list[int], float):
        """
        Finds the shortest path that visits all the nodes in the list
        :param node_lst: A list of nodes id's
        :return: A list of the nodes id's in the path, and the overall distance
        """
        print(self.isConnected())
        if self.isConnected() == False:
            return ([], math.inf)
        if len(node_lst) <= 1:
            return ([node_lst, 0])
        ans = []
        dist = 0
        for i in range(0, len(node_lst) - 1):
            curr = node_lst[i]
            next = node_lst[i + 1]
            k = (self.shortest_path(curr, next)[1])
            dist += self.shortest_path(curr, next)[0]
            for j in k:
                if j not in ans:
                    ans.append(j)
        p = (ans, dist)
        return p
