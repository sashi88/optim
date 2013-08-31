#from   pulp import *
import pulp 


prob = pulp.LpProblem("test1", pulp.LpMaximize)

# variables
x1 = pulp.LpVariable("x1", 0)
x2 = pulp.LpVariable("x2", 0)
x3 = pulp.LpVariable("x3", 0)
x4 = pulp.LpVariable("x4", 0)


# objective
prob += x1 + x2 + x3 + x4

# Constraints
prob += x1 <= 35000
prob += x2 <= 20000
prob += x3 <= 10000
prob += x4 <= 5000
prob += x3 + x4 == 10000
prob += x1 + x2 + x3 + x4 == 20000

pulp.GLPK().solve(prob)

# solution
for v in prob.variables():
	print v.name, "=", v.varValue

print "objective=", pulp.value(prob.objective)
