import networkx as nx
import pandas as pd
import os

class GraphBuilder:
    """
    Handles the creation and modification of football relational graphs.
    """
    
    @staticmethod
    def create_empty():
        """Creates a new empty NetworkX DiGraph."""
        return nx.DiGraph()

    @staticmethod
    def from_csv(csv_path):
        """
        Creates a graph from a tracking data CSV.
        Expected columns: x, y, s, a, dis, o, dir, event, nflId, displayName, jerseyNumber, position, frameId, team, playId
        """
        if not os.path.exists(csv_path):
            raise FileNotFoundError(f"CSV file not found: {csv_path}")
            
        df = pd.read_csv(csv_path)
        G = nx.DiGraph()
        
        # Group by frame to potentially handle time-series, but for now we take a snapshot or aggregate
        # In this simplified version, we'll build a graph for a specific frame or the 'event' frame
        
        for _, row in df.iterrows():
            node_id = str(row.get('nflId', row.get('displayName')))
            G.add_node(node_id, 
                       x=row.get('x'), 
                       y=row.get('y'), 
                       s=row.get('s'), 
                       position=row.get('position'),
                       team=row.get('team'),
                       role=row.get('role', 'unknown'))
            
        return G

    @staticmethod
    def add_player(G, player_id, attributes):
        """Adds or updates a player node in the graph."""
        G.add_node(player_id, **attributes)

    @staticmethod
    def add_relationship(G, source_id, target_id, edge_type, attributes=None):
        """Adds a directed edge between two nodes with a specific type (e.g., VECTOR, INFLUENCE)."""
        if attributes is None:
            attributes = {}
        attributes['type'] = edge_type
        G.add_edge(source_id, target_id, **attributes)

    @staticmethod
    def save_graphml(G, path):
        """Saves the graph in GraphML format."""
        nx.write_graphml(G, path)

    @staticmethod
    def load_graphml(path):
        """Loads a graph from a GraphML file."""
        return nx.read_graphml(path)
