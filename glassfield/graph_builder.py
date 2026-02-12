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
            node_id = str(row.get('displayName'))
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
    def extract_temporal_facts(csv_path):
        """
        Extracts temporal facts (attributes over time) from tracking CSV.
        Returns a list of pyreason.Fact objects.
        """
        import pyreason as pr
        df = pd.read_csv(csv_path)
        facts = []
        
        # Determine total timesteps
        max_frame = df['frameId'].max()
        
        # For each player, track their state
        for player_id in df['nflId'].unique():
            player_df = df[df['nflId'] == player_id]
            display_name = player_df['displayName'].iloc[0]
            pos = player_df['position'].iloc[0]
            
            # Static role fact
            facts.append(pr.Fact(f"{pos.lower()}({display_name}) : [1,1]", f"{display_name}_role_{pos}", 0, max_frame))
            
            # Dynamic position/speed facts (simplified for logic)
            for _, row in player_df.iterrows():
                t = int(row['frameId'])
                # Example: 'moving' predicate if speed > 5
                if row['s'] > 5:
                    facts.append(pr.Fact(f"moving({display_name}) : [1,1]", f"{display_name}_moving_{t}", t, t))
                
                # We could add spatial relations here too, or let PyReason compute them from coordinates
                # For now, let's just add 'deep' if x > 35
                if row['x'] > 35:
                    facts.append(pr.Fact(f"deep({display_name}) : [1,1]", f"{display_name}_deep_{t}", t, t))
                    
        return facts, max_frame
