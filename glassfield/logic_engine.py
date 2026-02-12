import pyreason as pr
import os
import networkx as nx

class LogicEngine:
    """
    Integrates with PyReason to perform temporal logic auditing on play graphs.
    """
    
    def __init__(self):
        # Initialize PyReason settings
        pr.settings.verbose = False
        pr.settings.atom_trace = True

    @staticmethod
    def load_rules_from_file(rule_path):
        """Loads rules from a .txt file and returns a list of rule strings."""
        if not os.path.exists(rule_path):
            raise FileNotFoundError(f"Rule file not found: {rule_path}")
        
        rules = []
        with open(rule_path, 'r') as f:
            for line in f:
                line = line.strip()
                if line and not line.startswith("//"):
                    rules.append(line)
        return rules

    @staticmethod
    def audit(play_graph, rule_text, facts=None, time_steps=None):
        """
        Runs the PyReason reasoning engine on the graph with the provided rules and optional facts.
        """
        import pyreason as pr
        # 1. Clear any previous state
        pr.reset()
        
        # 2. Load the Graph
        pr.load_graph(play_graph)
        
        # 3. Load Facts
        if facts:
            for fact in facts:
                pr.add_fact(fact)
        
        # 4. Load Rules
        # Support both single rule strings and lists of rules
        if isinstance(rule_text, str):
            pr.add_rule(pr.Rule(rule_text, "audit_rule"))
        elif isinstance(rule_text, list):
            for i, r in enumerate(rule_text):
                pr.add_rule(pr.Rule(r, f"audit_rule_{i}"))
        
        # 5. Run Reasoning
        # If time_steps is None, it will run until convergence (usually -1)
        # but for football plays we usually have a fixed window
        steps = time_steps if time_steps is not None else -1
        interpretation = pr.reason(timesteps=steps)
        
        return interpretation
