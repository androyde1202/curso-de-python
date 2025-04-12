#exercicio1
#numero=int(input("digite um numero fara faroria-lo:"))
#fatorial= 1
#for q in range(1,numero+1,1):
#    fatorial= fatorial*q 
#print(fatorial)
#exercicio2
#for w in range (2,101,2):
#   print(w)
#exercicio 3
#stop=int(input(" escolha um numero para somarmos todos os numeros anteriores a ele:"))
#soamador=0
#for e in range(1,stop +1,1):
#    soamador = soamador +e
#print(f"a soma de todos o numeros interiores a ele é {soamador}") 
#exercicio4
n=int(input("qual numero você deseja ver a tabuada:"))
multiplicador=int(input("até qual numero você deseja ver os multiplos:"))
for r in range(0,multiplicador+1,1):
    print(f"{n} * {r} = {n*r}")