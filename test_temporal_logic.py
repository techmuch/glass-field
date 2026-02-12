from glassfield import GraphBuilder, LogicEngine
import pyreason as pr
import os

def main():
    print("--- Stage 1: Relational Map & Temporal Fact Extraction ---")
    csv_path = "game_data/sample_play.csv"
    G = GraphBuilder.from_csv(csv_path)
    facts, max_steps = GraphBuilder.extract_temporal_facts(csv_path)
    
    # QB_1 is NOT pressured (static)
    # If we don't add it, NOT pressured(y) will be true by default in Open World logic
    # but let's be explicit if we wanted to test the opposite
    
    print(f"Extracted {len(facts)} facts across {max_steps} timesteps.")

    print("\n--- Stage 2: Temporal Reasoning ---")
    engine = LogicEngine()
    rules = engine.load_rules_from_file("rules/offensive_spacing.txt")
    print(f"Loaded {len(rules)} rules.")
    
    interpretation = engine.audit(G, rules, facts=facts, time_steps=max_steps)

    print("\n--- Stage 3: Structural Vulnerability Report ---")
    # Check for 'vulnerable' predicate
    results = pr.filter_and_sort_nodes(interpretation, ['vulnerable'])

    for t in range(max_steps + 1):
        print(f"Frame {t}:")
        found = False
        if t < len(results):
            df = results[t]
            if not df.empty and 'vulnerable' in df.columns:
                for _, row in df.iterrows():
                    if row['vulnerable'][0] >= 0.9:
                        print(f"  [!] {row['component']} is VULNERABLE!")
                        found = True
        
        if not found:
            print("  Structure sound.")

if __name__ == "__main__":
    main()
