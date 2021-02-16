# -*- coding: utf-8 -*

def check(s):
    open = ('(', '[', '{')
    closed = (')', ']', '}')
    stack = []
    for i in s:
        if i in open:
            stack.append(i)
        if i in closed:    
            if len(stack) == 0:
                False
            if stack[-1] == open[closed.index(i)]:
                stack = stack[:-1]  
            else: return False  
    return True
print(check("{}[(]"))
