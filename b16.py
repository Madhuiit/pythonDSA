#flaaten  nexted list
nested = [[1,2,3],[1,2]]

flat = [x for sub in nested for x in sub]
print(flat)