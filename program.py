from ortools.sat.python import cp_model

model = cp_model.CpModel()

# vars declaration 3x4
x = {}
for r in range(3):
    for c in range(4):
        x[(r,c)] = model.new_int_var(1, 12, f"x_{r}_{c}")

# starting values constraint
model.add(x[(0,1)] == 6)    # B1
model.add(x[(1,0)] == 8)    # A2
model.add(x[(2,2)] == 3)    # C3

# every value different constraint
model.add_all_different(x.values())

# the sum of rows constraint
model.add(x[(0,0)] + x[(0,1)] + x[(0,2)] + x[(0,3)] == 30)
model.add(x[(1,0)] + x[(1,1)] + x[(1,2)] + x[(1,3)] == 18)
model.add(x[(2,0)] + x[(2,1)] + x[(2,2)] + x[(2,3)] == 30)

# the sum of columns constraint
model.add(x[(0,0)] + x[(1,0)] + x[(2,0)] == 27)
model.add(x[(0,1)] + x[(1,1)] + x[(2,1)] == 16)
model.add(x[(0,2)] + x[(1,2)] + x[(2,2)] == 10)
model.add(x[(0,3)] + x[(1,3)] + x[(2,3)] == 25)

solver = cp_model.CpSolver()
status = solver.solve(model)