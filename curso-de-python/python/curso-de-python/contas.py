n=int(input("qual numero você deseja ver a tabuada:"))
multiplicador=int(input("até qual numero você deseja ver os multiplos:"))
for r in range(0,multiplicador+1,1):
    print(f"{n} * {r} = {n*r}")