"""Simplex Tableau Linear Programming Solver.
100% Python Standard Library.
"""

class SimplexSolver:
    """Solves standard LP: Maximize c^T x subject to A x <= b, x >= 0."""
    @staticmethod
    def solve(c, A, b):
        m = len(A)
        n = len(c)
        
        tableau = []
        for i in range(m):
            slack = [1.0 if j == i else 0.0 for j in range(m)]
            tableau.append(list(A[i]) + slack + [float(b[i])])
            
        obj_row = [-float(val) for val in c] + [0.0] * m + [0.0]
        tableau.append(obj_row)
        
        basis = [n + i for i in range(m)]
        
        max_iters = 100
        for _ in range(max_iters):
            pivot_col = -1
            min_val = -1e-8
            for j in range(n + m):
                if tableau[-1][j] < min_val:
                    min_val = tableau[-1][j]
                    pivot_col = j
                    
            if pivot_col == -1:
                break
                
            pivot_row = -1
            min_ratio = float('inf')
            for i in range(m):
                a_ij = tableau[i][pivot_col]
                if a_ij > 1e-8:
                    ratio = tableau[i][-1] / a_ij
                    if ratio < min_ratio:
                        min_ratio = ratio
                        pivot_row = i
                        
            if pivot_row == -1:
                return {"status": "unbounded", "optimal_value": None, "x": None}
                
            pivot_val = tableau[pivot_row][pivot_col]
            for j in range(len(tableau[0])):
                tableau[pivot_row][j] /= pivot_val
                
            for i in range(m + 1):
                if i != pivot_row:
                    factor = tableau[i][pivot_col]
                    for j in range(len(tableau[0])):
                        tableau[i][j] -= factor * tableau[pivot_row][j]
                        
            basis[pivot_row] = pivot_col
            
        x = [0.0] * n
        for i in range(m):
            if basis[i] < n:
                x[basis[i]] = round(tableau[i][-1], 5)
                
        opt_val = round(tableau[-1][-1], 5)
        return {"status": "optimal", "optimal_value": opt_val, "x": x}
