def fatorial(B):
    if B == 0:
     return 1
    else :
       return B * fatorial(B-1)
x=int(input("digite o numero para calcular o fatorial:"))
print (fatorial(x))