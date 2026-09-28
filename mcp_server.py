"""MCP stdio server for Simplex LP Solver."""
import sys
import json

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

from client import SimplexSolver

def handle_rpc(request):
    req_id = request.get("id")
    method = request.get("method")
    params = request.get("params", {})

    if method == "tools/list":
        return {
            "jsonrpc": "2.0",
            "id": req_id,
            "result": {
                "tools": [
                    {
                        "name": "solve_linear_program",
                        "description": "Solve LP: Maximize c^T x subject to A x <= b, x >= 0 via Simplex",
                        "inputSchema": {
                            "type": "object",
                            "properties": {
                                "c": {"type": "array", "items": {"type": "number"}},
                                "A": {"type": "array", "items": {"type": "array", "items": {"type": "number"}}},
                                "b": {"type": "array", "items": {"type": "number"}}
                            },
                            "required": ["c", "A", "b"]
                        }
                    }
                ]
            }
        }
    elif method == "tools/call":
        name = params.get("name")
        args = params.get("arguments", {})
        if name == "solve_linear_program":
            c = args.get("c", [])
            A = args.get("A", [])
            b = args.get("b", [])
            res = SimplexSolver.solve(c, A, b)
            return {"jsonrpc": "2.0", "id": req_id, "result": res}
        return {"jsonrpc": "2.0", "id": req_id, "error": {"code": -32601, "message": f"Method {name} not found"}}
    return {"jsonrpc": "2.0", "id": req_id, "error": {"code": -32600, "message": "Invalid request"}}

def main():
    for line in sys.stdin:
        if not line.strip():
            continue
        try:
            req = json.loads(line)
            res = handle_rpc(req)
            sys.stdout.write(json.dumps(res) + "\n")
            sys.stdout.flush()
        except Exception as e:
            sys.stdout.write(json.dumps({"jsonrpc": "2.0", "error": {"code": -32700, "message": str(e)}}) + "\n")
            sys.stdout.flush()

if __name__ == "__main__":
    main()
