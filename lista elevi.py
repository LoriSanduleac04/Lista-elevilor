with open ('listainitiala.txt','r') as h:
    a=str(h.read())
    b=a.split()
with open ('listafinala.txt','w') as h:
    h.write(str(sorted(b)))