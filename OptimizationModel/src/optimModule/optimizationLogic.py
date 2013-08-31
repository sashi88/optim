import pulp 
import result
import tkMessageBox


# def values(a,b,c):
#     print a + b + c
   
def optimLogic(excessNachwa,capacityNW,NW_LowLevel,NW_HigherLevel,MalwathuOya,SpecialCanal):
    prob = pulp.LpProblem("test1", pulp.LpMaximize)
    #logging.critical("came here !!!!!!!!")
    # variables
    x1 = pulp.LpVariable("x1", 0)
    x2 = pulp.LpVariable("x2", 0)
    x3 = pulp.LpVariable("x3", 0)
    x4 = pulp.LpVariable("x4", 0)

    # objective
    prob += x1 + x2 + x3 + x4
    
    # Constraints
    prob += x1 <= MalwathuOya
    prob += x2 <= SpecialCanal
    prob += x3 <= NW_HigherLevel
    prob += x4 <= NW_LowLevel
    prob += x3 + x4 == capacityNW
    prob += x1 + x2 + x3 + x4 == excessNachwa
#     prob += x3 + x4 == 10000
#     prob += x1 + x2 + x3 + x4 == 20000

    pulp.GLPK().solve(prob)
    
    i=0
    valueList=[]
    # solution
    for v in prob.variables():
        print v.name, "=", v.varValue
        valueList.insert(i, v.varValue) 
        i=i+1
        
    print "objective=", pulp.value(prob.objective)
    objtve =pulp.value(prob.objective)
    
    if (objtve != 0):
        result.viewOutput(valueList[0],valueList[1],valueList[2],valueList[3],objtve)
    else:
        tkMessageBox.showinfo("Warning", "Sorry !!! There is no optimum solution")
        
    
    
# def optimAlgo(x1,x2,x3):
    
    
#     prob1 = LpProblem("test1", LpMaximize)
# 
#     # variables
#     x1 = LpVariable("x1", 1)
#     x2 = LpVariable("x2", 0)
#     x3 = LpVariable("x3", 0)
#     x4 = LpVariable("x4", 0)
# 
# 
#     # objective
#     prob1 += x1 + x2 + x3 + x4
# 
#     # Constraints
#     prob1 += 0 < x1 <= 35000
#     prob1 += 0 < x2 <= 20000
#     prob1 += 0 < x3 <= 10000
#     prob1 += 0 < x4 <= 5000
#     prob1 += x3 + x4 == 15000
#     prob1 += x1 + x2 + x3 + x4 == 50000
# 
#     GLPK().solve(prob1)
#     print "***************************"
#     # solution
#     for v in prob1.variables():
#         print v.name, "=", v.varValue
# 
#     print "objective=", value(prob1.objective)
#     