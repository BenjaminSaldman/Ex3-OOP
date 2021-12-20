from src.GraphAlgoInterface import GraphAlgoInterface
from src.GraphInterface import GraphInterface
from src.DiGraph import DiGraph
import json


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
