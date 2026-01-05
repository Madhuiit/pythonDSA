# sort dictionary by values
d = {'a':2,'b':1}

print(dict(sorted(d.items(),key=lambda x : x[1])))