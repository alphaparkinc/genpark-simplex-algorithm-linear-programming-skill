# Simplex Linear Programming Skill

Canonical Simplex tableau solver for constrained linear optimization problems.

```mermaid
flowchart TD
    Problem["Max c^T x s.t. Ax <= b, x >= 0"] --> Tableau["Construct Tableau with Slack Vars"]
    Tableau --> PivotCol["Choose Entering Col (Most Negative in Obj)"]
    PivotCol --> PivotRow["Choose Leaving Row (Minimum Ratio Test)"]
    PivotRow --> Elimination["Gauss-Jordan Row Elimination"]
    Elimination --> OptCheck{"Negative Coeffs Remain?"}
    OptCheck -- Yes --> PivotCol
    OptCheck -- No --> Optimal["Extract Optimal Solution x* and Value z*"]
```

## Features
- **100% Python Standard Library**: Pure matrix row reduction.
- **Unbounded & Feasibility Detection**: Built-in edge condition checks.
- **MCP Server Ready**: Instant stdio access for operational research.
