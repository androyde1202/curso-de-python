class vendedor ():
    def __init__(self,nome):
        self.nome = nome
        self.venda = 0
    def vendeu(self,valor):
        self.venda += valor
    
    def bateumeta(self,meta):
        if self.venda >= meta:
            print(self.nome,"bateu meta")
        else :
            print(self.nome, "não bateu meta")
nomevendedor=input("qual nome do vendedor?")
vendeuMes=float(input("quanto o vendedor vendeu?"))
meta=float(input("quala meta do vendedor:?"))
vendedor01=vendedor(nomevendedor)
vendedor01.vendeu(vendeuMes)
vendedor01.bateumeta(meta)

nomevendedor=input("qual nome do vendedor?")
vendeuMes=float(input("quanto o vendedor vendeu?"))
meta=float(input("quala meta do vendedor:?"))
vendedor02=vendedor(nomevendedor)
vendedor02.vendeu(vendeuMes)
vendedor02.bateumeta(meta)

if vendedor01.venda > vendedor02.venda:
    print(f"{vendedor01} vendeu mais que {vendedor02}")
else:
    print(f"{vendedor02} vendeu mais que {vendedor01}")