from glassfield import GraphBuilder, LogicEngine, SignalIntel
import pyreason as pr
import os

def main():
    print("--- Stage 0: Signal Intelligence ---")
    context = SignalIntel.fetch_context(team="Chiefs", opponent="Ravens")

    print("\n--- Stage 1: Relational Map ---")
    G = GraphBuilder.create_empty()
    G.add_node("WR_01")
    G.add_node("DB_01")
    G.add_edge("WR_01", "DB_01", type="remote")

    print("\n--- Stage 2: Logic Engine (PyReason) ---")
    pr.reset()
    pr.load_graph(G)
    
    # Correct constructor based on help(): Fact(fact_text, name, start_time, end_time)
    pr.add_fact(pr.Fact("receiver(WR_01) : [1,1]", "wr-receiver-fact", 0, 1))
    
    # Try a rule with a static component
    rule = "open(WR_01) : [1,1] <- receiver(WR_01)"
    pr.add_rule(pr.Rule(rule, "test_rule"))
    
    interpretation = pr.reason(timesteps=1)
    
    print("\n--- Stage 3: Intelligence Output ---")
    df = pr.filter_and_sort_nodes(interpretation, ['open'])
    print(df)

if __name__ == "__main__":
    main()
