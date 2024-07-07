from constraint import Problem, AllDifferentConstraint

# Example of CSP using the 'constraint' library
problem = Problem()
problem.addVariable('A', [1, 2, 3])
problem.addVariable('B', [4, 5, 6])
problem.addConstraint(AllDifferentConstraint())

solutions = problem.getSolutions()
print(solutions)
