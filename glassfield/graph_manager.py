import os
import networkx as nx
from .graph_builder import GraphBuilder

class GraphManager:
    """
    Manages a collection of graphs, allowing for loading, saving, and quick access.
    """
    def __init__(self):
        self.graphs = {}

    def add_graph(self, name, graph):
        """Adds a graph to the manager."""
        self.graphs[name] = graph

    def get_graph(self, name):
        """Retrieves a graph by name."""
        return self.graphs.get(name)

    def remove_graph(self, name):
        """Removes a graph from the manager."""
        if name in self.graphs:
            del self.graphs[name]

    def list_graphs(self):
        """Returns a list of managed graph names."""
        return list(self.graphs.keys())

    def save_all(self, directory):
        """Saves all managed graphs to a directory in GraphML format."""
        if not os.path.exists(directory):
            os.makedirs(directory)
        for name, G in self.graphs.items():
            path = os.path.join(directory, f"{name}.graphml")
            GraphBuilder.save_graphml(G, path)

    def load_from_directory(self, directory):
        """Loads all .graphml files from a directory into the manager."""
        if not os.path.exists(directory):
            return
        for filename in os.listdir(directory):
            if filename.endswith(".graphml"):
                name = os.path.splitext(filename)[0]
                path = os.path.join(directory, filename)
                self.graphs[name] = GraphBuilder.load_graphml(path)
