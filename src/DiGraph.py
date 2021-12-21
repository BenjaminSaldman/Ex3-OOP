from src.GraphInterface import GraphInterface
from src.Node import Node


class DiGraph(GraphInterface):
    def __init__(self):
        self.Nodes = {}
        self.Edges = {}
        self.MC = 0
        self.edgeCounter = 0

    def v_size(self) -> int:
        return len(self.Nodes)

    def e_size(self) -> int:
        return self.edgeCounter;

    def get_all_v(self) -> dict:
        return self.Nodes

    def all_in_edges_of_node(self, id1: int) -> dict:
        """return a dictionary of all the nodes connected to (into) node_id ,
        each node is represented using a pair (other_node_id, weight)
         """
        ans = {}
        if id1 in self.Nodes:
            for i, j in self.Edges.items():
                if id1 in j:
                    ans[i] = j[id1]
            return ans
        return ans

    def all_out_edges_of_node(self, id1: int) -> dict:
        """return a dictionary of all the nodes connected from node_id , each node is represented using a pair
        (other_node_id, weight)
        """
        if id1 in self.Nodes:
            return self.Edges[id1]
        return {};

    def get_mc(self) -> int:
        """
        Returns the current version of this graph,
        on every change in the graph state - the MC should be increased
        @return: The current version of this graph.
        """
        return self.MC

    def add_edge(self, id1: int, id2: int, weight: float) -> bool:
        """
        Adds an edge to the graph.
        @param id1: The start node of the edge
        @param id2: The end node of the edge
        @param weight: The weight of the edge
        @return: True if the edge was added successfully, False o.w.
        Note: If the edge already exists or one of the nodes dose not exists the functions will do nothing
        """
        if id1 in self.Nodes and id2 in self.Nodes and id2 not in self.Edges[id1]:

            self.Edges[id1][id2] = weight
            self.MC += 1
            self.edgeCounter += 1
            return True
        return False

    def add_node(self, node_id: int, pos: tuple = None) -> bool:
        """
        Adds a node to the graph.
        @param node_id: The node ID
        @param pos: The position of the node
        @return: True if the node was added successfully, False o.w.
        Note: if the node id already exists the node will not be added
        """
        if node_id not in self.Nodes:
            n = Node(node_id, pos)
            self.Nodes[node_id] = n
            self.Edges[node_id] = {}
            return True
        return False

    def remove_node(self, node_id: int) -> bool:
        """
        Removes a node from the graph.
        @param node_id: The node ID
        @return: True if the node was removed successfully, False o.w.
        Note: if the node id does not exists the function will do nothing
        """
        if node_id in self.Nodes:
            into = self.all_in_edges_of_node(node_id)
            self.MC += len(self.Edges[node_id])
            self.edgeCounter -= len(self.Edges[node_id])
            del self.Nodes[node_id]
            for i in into.keys():
                self.remove_edge(i, node_id)
            self.Nodes.pop(node_id)
            self.MC += 1
            return True;
        return False

    def remove_edge(self, node_id1: int, node_id2: int) -> bool:
        """
        Removes an edge from the graph.
        @param node_id1: The start node of the edge
        @param node_id2: The end node of the edge
        @return: True if the edge was removed successfully, False o.w.
        Note: If such an edge does not exists the function will do nothing
        """
        if node_id1 in self.Nodes and node_id2 in self.Nodes:
            if node_id2 in self.Edges[node_id1]:
                self.Edges[node_id1].pop(node_id2)
                self.edgeCounter -= 1
                self.MC += 1
                return True
            return False
        return False

