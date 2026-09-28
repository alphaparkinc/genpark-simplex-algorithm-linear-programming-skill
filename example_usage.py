"""Example demonstrating Simplex LP optimization."""
from client import SimplexSolver

def main():
    c = [3.0, 2.0]
    A = [[2.0, 1.0], [1.0, 1.0], [1.0, 0.0]]
    b = [100.0, 80.0, 40.0]
    res = SimplexSolver.solve(c, A, b)
    print("Simplex Optimization Result:")
    print("  Status:", res["status"])
    print("  Optimal Value:", res["optimal_value"])
    print("  Optimal Solution x:", res["x"])

if __name__ == "__main__":
    main()
