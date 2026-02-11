# Project Glass-Field: The Neuro-Symbolic Football Analyst

## 1. The Mission

Project Glass-Field operates on a simple premise: Standard analytics are opaque; logic is transparent.

In the current landscape of sports intelligence, teams rely heavily on descriptive data—heat maps, completion percentages, and aggregate "expected points" models. While these metrics tell you who was where and what happened, they fail to explain the structural "why." They cannot distinguish between a coverage bust caused by physical inability versus one caused by a logical error in decision-making.

Glass-Field changes the paradigm by focusing on structural transparency. We do not simply track coordinates; we map the logic of space. By converting a football game into a dynamic, relational GraphML network and applying PyReason (a state-of-the-art temporal logic framework), we treat the field as a solvable equation.

**The Core Thesis:** The field is not just a physical plane; it is a logical system of constraints and opportunities. By treating the game as a transparent graph, we can detect "ghost" vulnerabilities—high-value openings that exist mathematically in the defense's logic, even if the offense failed to exploit them in the moment. This allows coaches to separate "outcome" from "process," identifying the plays that should have worked.

## 2. The Architecture

Glass-Field operates on a sophisticated 4-stage intelligence pipeline designed to translate chaos into axioms. We combine Micro-Level Tracking (on-field data) with Macro-Level Signals (off-field intelligence) to form a complete probabilistic picture.

### Stage 0: Signal Intelligence (OSINT Ingestion)
Before the game begins, we establish the "Priors." We aggregate external data to weigh the logic engine's confidence intervals.
*   **News Scrapers (LLM-Driven):** We deploy LLM agents to scrape beat writer reports and injury updates, extracting latent variables like "Locker Room Morale" or "Hidden Injury Risks" that official reports miss.
*   **Prediction Markets:** We integrate real-time odds from markets (e.g., Polymarket, Kalshi) to derive the "Crowd Wisdom" probability of specific game scripts (e.g., "Heavy Run Game script implied probability: 65%").

### Stage 1: The Relational Map (GraphML)
We ingest raw tracking data (Next Gen Stats, GPS CSVs) and transmute it into GraphML. This is not a static picture; it is a time-series graph.
*   **Nodes (Entities):** Every player, the ball, and abstract "Strategic Zones" (e.g., Deep Left Third, The A-Gap).
*   **Edges (Interactions):** We draw invisible lines that represent the game's physics and logic: "Vectors of Intent," "Blocking Constraints," and "Influence" (gravity).

### Stage 2: Reasoning (The Logic Engine)
The graph is fed into PyReason, which applies "Open World" reasoning. Unlike standard code that crashes on uncertainty, PyReason handles "Annotated Logic."
*   **The Axiom Layer:** We define football strategy as immutable logic rules.
*   **Context-Aware Logic:** The engine adjusts rules based on OSINT. 
    *   *Example:* IF (News_Sentiment_QB_Shoulder == "Concern") THEN (Deep_Pass_Probability_Weight *= 0.7).
*   **Temporal reasoning:** The engine audits the play across time steps ($t=0$ to $t=n$), detecting exactly when a defensive structure becomes logically unsound.

### Stage 3: Intelligence (The Structural Output)
The system outputs a "Structural Vulnerability Report." This is not a box score; it is a diagnostic readout flagging specific edge-failures. It identifies matchups where the logic of the defense broke down, providing a probability interval of failure (e.g., "92% chance of separation") regardless of whether the Quarterback actually threw the ball.

## 3. Getting Started

To ensure scientific rigor and reproducibility in our data science workflow, we use **Pixi** for hermetic environment management and **Jupyter Lab** as our primary tactical workbench.

### Prerequisites
*   **Pixi (Package Manager)** - [Install Pixi](https://pixi.sh)
*   *Why Pixi?* It handles both Python dependencies and system-level libraries (like graph visualization tools) in a lock-file, ensuring that "it works on my machine" means it works on the coaching staff's machines too.

### Installation
```bash
git clone https://github.com/yourusername/project-glass-field.git
cd project-glass-field

# Pixi will automatically install Python 3.11, PyReason, NetworkX, and Jupyter Lab
# creating an isolated environment for the project.
pixi install
```

### Launch the Tactical Workbench
To start the interactive environment for analyzing plays, visualizations, and logic auditing:
```bash
pixi run jupyter lab
```

### Quick Start: Analyzing a Single Play (in Notebook)
Open `analysis_notebook.ipynb` in Jupyter Lab and run the following neuro-symbolic audit:

```python
from glassfield import GraphBuilder, LogicEngine, SignalIntel

# 1. Fetch External Signals (OSINT)
# Scrapes latest news and checks market implied probabilities
context = SignalIntel.fetch_context(team="Chiefs", opponent="Ravens")
print(f"Market Implied Blitz Rate: {context.blitz_probability}")

# 2. Build the Transparent Graph from a Play ID
# This converts coordinate data into a NetworkX graph with 'Vector' and 'Influence' edges.
play_graph = GraphBuilder.from_csv("game_data/week_1_play_45.csv")

# 3. Define the "Zone Logic" Rule with Context
# We load a rule that defines "being open" but adjust thresholds based on the opposing defense's market profile.
zone_rule = LogicEngine.load_rule("rules/offensive_spacing.txt", context=context)

# 4. Run the Audit
# PyReason scans the graph across time t=0 to t=5.0s
opportunity = LogicEngine.audit(play_graph, zone_rule)

print(f"Structural Opportunity: {opportunity.score}")
# Output: "High-Value Opening Detected at Zone: Deep_Left_Third (Probability: 0.92)"
# Analysis: "The Free Safety failed to deepen relative to WR_1's velocity vector at t=2.4s."
```

## 4. The Data Structure (GraphML)

We represent plays using a custom GraphML schema designed for GNN (Graph Neural Network) compatibility. See `docs/schema_v1.xml` for the full definition.

### Node Attributes (The State):
*   **id:** Unique Player ID (e.g., "QB_01", "Def_05")
*   **role:** The functional role ("Passer", "Blocker", "Rusher", "Spy")
*   **vision:** Float $[0.0 - 1.0]$ representing the "Field of View" cone.
*   **fatigue:** Float $[0.0 - 1.0]$ representing dynamic stamina decay over the game.
*   **morale:** Float $[0.0 - 1.0]$ derived from OSINT analysis of sideline behavior and news reports.

### Edge Types (The Relationships):
*   **VECTOR:** The intended path of the ball or player based on current velocity.
*   **CONSTRAINT:** A physical or logical block. A successful block is a high-weight constraint; a failed block is a decaying constraint.
*   **INFLUENCE:** The "Gravity" of a player. A star Receiver (WR1) has high "Influence" edges that warp the behavior of nearby Defensive Back nodes, drawing double coverage.

## 5. Roadmap (2026)

*   [x] **Alpha:** Basic GraphML conversion of static plays from CSV tracking data.
*   [ ] **Beta:** Full integration with PyReason for Temporal Logic. This includes tracking route development from $t=0$ to $t=3.5$, identifying the exact millisecond a "break" occurs.
*   [ ] **Feature:** Signal Intelligence Module – Build the LLM scraper pipeline to ingest news/market data and output normalized "Context Vectors."
*   [ ] **Release 1.0:** "The Glass Dashboard" – A visual tool for coaches to see the "hidden" edges of influence and replay "Counter-Factual" scenarios (e.g., "What if the Safety had reacted 0.5s faster?").
*   [ ] **Release 2.0:** Automated Playbook Generation – Using the logic engine to suggest play designs that mathematically maximize stress on specific defensive graph structures.

## 6. Contributing

We operate at the intersection of High-Performance Computing and Football Strategy. We welcome contributions from:
*   **Data Engineers:** To optimize GNN models and graph ingestion pipelines.
*   **Football Strategists:** To help define the "Logic Rules" (axioms) that the engine uses to judge success and failure.
*   **Logic Programmers:** To optimize PyReason rules for speed and temporal accuracy.

**Contribution Workflow:**
1. Fork the repo.
2. Create your feature branch (`git checkout -b feature/NewLogic`).
3. Commit your changes (`git commit -m 'Add NewLogic'`).
4. Push to the branch (`git push origin feature/NewLogic`).
5. Open a Pull Request.

## 7. License

Distributed under the MIT License. See `LICENSE` for more information.
