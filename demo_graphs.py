from glassfield import GraphBuilder, GraphManager
import networkx as nx

def main():
    # 1. Initialize Manager
    manager = GraphManager()
    
    # 2. Build a new graph from scratch
    G1 = GraphBuilder.create_empty()
    GraphBuilder.add_player(G1, "QB_01", {"role": "Passer", "team": "Home", "x": 10, "y": 25})
    GraphBuilder.add_player(G1, "WR_01", {"role": "Receiver", "team": "Home", "x": 30, "y": 10})
    GraphBuilder.add_relationship(G1, "QB_01", "WR_01", "VECTOR", {"strength": 0.8})
    
    manager.add_graph("play_1", G1)
    
    # 3. Modify an existing graph
    G_to_mod = manager.get_graph("play_1")
    GraphBuilder.add_player(G_to_mod, "DB_01", {"role": "Defender", "team": "Away", "x": 28, "y": 12})
    GraphBuilder.add_relationship(G_to_mod, "DB_01", "WR_01", "INFLUENCE", {"type": "coverage"})
    
    # 4. Create another graph
    G2 = GraphBuilder.create_empty()
    GraphBuilder.add_player(G2, "RB_01", {"role": "Rusher", "team": "Home", "x": 15, "y": 25})
    manager.add_graph("play_2", G2)
    
    # 5. List and Verify
    print(f"Managed graphs: {manager.list_graphs()}")
    for name in manager.list_graphs():
        G = manager.get_graph(name)
        print(f"Graph '{name}' has {G.number_of_nodes()} nodes and {G.number_of_edges()} edges.")

    # 6. Save and Load Test
    manager.save_all("data_test")
    print("Saved all graphs to 'data_test/'")
    
    new_manager = GraphManager()
    new_manager.load_from_directory("data_test")
    print(f"Loaded graphs into new manager: {new_manager.list_graphs()}")

if __name__ == "__main__":
    main()
