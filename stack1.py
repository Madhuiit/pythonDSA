def reversed_String(s):
    stack = []
    for i in  s:
        stack.append(i)
    reversed_S = ''




    while stack:
        reversed_S+=stack.pop()
    return reversed_S


print(reversed_String("hellow"))
