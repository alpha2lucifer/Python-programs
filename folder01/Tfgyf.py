with open("var.txt") as f:
    a=f.read()
    ic=0
    ec=0
    for i in a:
        if i.upper()=='I':
            ic=ic+1
        elif i.upper()=='E':
            ec=ec+1
print (f"i count={ic}")
print (f"e count={ec}")