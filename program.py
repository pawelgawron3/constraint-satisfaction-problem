from ortools.linear_solver import pywraplp

solver = pywraplp.Solver.CreateSolver('SCIP')

# vars declaration 3x4
x = {}
for r in range(3):
    for c in range(4):
        x[(r,c)] = solver.IntVar(1, 12, f"x_{r}_{c}")

# starting values constraint
solver.Add(x[(0,1)] == 6)    # B1
solver.Add(x[(1,0)] == 8)    # A2
solver.Add(x[(2,2)] == 3)    # C3

# the sum of rows constraint
solver.Add(x[(0,0)] + x[(0,1)] + x[(0,2)] + x[(0,3)] == 30)
solver.Add(x[(1,0)] + x[(1,1)] + x[(1,2)] + x[(1,3)] == 18)
solver.Add(x[(2,0)] + x[(2,1)] + x[(2,2)] + x[(2,3)] == 30)

# the sum of columns constraint
solver.Add(x[(0,0)] + x[(1,0)] + x[(2,0)] == 27)
solver.Add(x[(0,1)] + x[(1,1)] + x[(2,1)] == 16)
solver.Add(x[(0,2)] + x[(1,2)] + x[(2,2)] == 10)
solver.Add(x[(0,3)] + x[(1,3)] + x[(2,3)] == 25)

status = solver.Solve()

if status == pywraplp.Solver.OPTIMAL:
    for r in range(3):
        row = []
        for c in range(4):
            row.append(int(x[(r,c)].solution_value()))
        print(row)
else:
    "No solution!"