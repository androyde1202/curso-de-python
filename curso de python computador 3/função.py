#exemplo 1
#def exibirnome():
#    print("meu nome é andrey")
#    print("hoje é sabado")
#
#exibirnome()
#variavel local e global
#nome="X"
#sobrenome="Y"
#def cadastro():
#    print("ola voce fara o cadastro na loja XP10")
#    nome=input("digite seu nome:") #essa variavel só existe na função cadastro
#    sobrenome=input("digite seu sobrenome:")#essa variavel só funciona na função cadastro 
#    print(nome)
#    print(sobrenome)
#cadastro()
#print("cadastro foi finalizado")
#print(nome)
#print(sobrenome) #se criarmos uma variavel fora ela sera uma variavel diferente com o mesmo nome
#teste global e local2
#def somar(a,b):
#    print(a+b)
#a=int(input("digite o primero numero:"))
#b=int(input("digite o segundo numero:"))
#somar(a,b)
#exercicios multiplicar função
#X=float(input("digite o primeiro numero:"))
#Y=float(input("digite o segundo numero:"))
#=float(input("digite o terceiro numero:"))
#operacao=input("coloque + para adição e * para multiplicação:")
#def resultado(x,y,z,operacao):
#    if operacao=="+":
#        soma=X+Y+Z
#        print(X,"+",Y,"+",Z,"=",soma)
#    else :
#        multiplicacao=X*Y*Z
#        print(X,"*",Y,"*",Z,"=",multiplicacao)
#
#resultado(X,Y,Z,operacao)
#consessionaria
#valordocarro=float(input("qual o valor do carro?"))
#comissao=float(input("quantos porcento do valor do carro vendido so funcionariso ganham?"))
#imposto=float(input("quanto porcento de impodto pelo carro vendido terrei que pagar?"))
#def calcularlucro(valordocarro,comissao,imposto):
#    comissao = comissao/100
#    imposto = imposto/100
#    lucro=(valordocarro-(valordocarro*imposto))-valordocarro*comissao
#    comissao=comissao*100
#    imposto*100
#    print("com o valor bruto de ",valordocarro,"com um imposto de ",imposto,"% e com uma comissão de ",comissao,"% o lucro foi",lucro,"da moeda utilizada")
#calcularlucro(valordocarro,comissao,imposto)
#para multiplcar 
#n1=float(input("qual numero você deseja ver a tabuada:"))
#n2=int(input("até qual numero você deseja ir:"))
#def tabuada(n1,n2):
#    for r in range(n2+1):
#        print(n1,"*",r,"=",n1 * r )
#tabuada(n1,n2)
#esfregador de media melho na cara
#p1=str(input("nome do primeiro aluno:"))
#p1n1=float(input("primeira nota do primeiro aluno:"))
#p1n2=int(input("segunda nota do primeiro aluno:"))
#p2=str(input("nome do segundo aluno:"))
#p2n1=float(input("primeira nota do segundo aluno:"))
#p2n2=int(input("segunda nota do segundo aluno:"))
#p3=str(input("nome do terceiro aluno:"))
#p3n1=float(input("primeira nota do terceiro aluno:"))
#p3n2=int(input("segunda nota do terceiro aluno:"))
#def melhormedia(p1,p1n1,p1n2,p2,p2n1,p2n2,p3,p3n1,p3n2):
#    mediap1=(p1n1+p1n2)/2 
#    mediap2=(p2n1+p2n2)/2 
#    mediap3=(p3n1+p3n2)/2 
#    if mediap1> mediap2 and mediap1>mediap3:
#        print(f"o aluno {p1} tem a maior media sendo ela {mediap1}")
#    elif mediap2>mediap1 and mediap2>mediap3:
#        print(f"o aluno {p2} tem a maior media sendo ela {mediap2}")
#    elif mediap3>mediap2 and mediap3>mediap1:
#        print(f"o aluno {p3} tem a maior media sendo ela {mediap3}")
#    else: 
#        print(" dois ou tres alunos tem a mesma media sendo as mais altas")
#melhormedia(p1,p1n1,p1n2,p2,p2n1,p2n2,p3,p3n1,p3n2)
#programa caminhoneiros
#placa=str(input("qual a placa do seu caminhão no estilo ???-????:"))
#kminicial=int(input("quantos km tinha no caminhão no começo da viagem?"))
#kmfinal=float(input("quantos kilometros tem neste momento?"))
#valorgasolina=float(input("quanto custou a gasolina por litro?"))
#quantidade=float(input("quantos litros foram gastos?"))
#def consumo(placa,kminicial,kmfinal,valorgasolina,quantidade):
#    distancia=kmfinal-kminicial
#    mediakmpl=quantidade/distancia
#    gastos=quantidade*valorgasolina
#    print(f"seu caminhão com a placa {placa} rodou {distancia} KM fazendo uma media de {mediakmpl}KM/litro, gastando {gastos} reais")
#consumo(placa,kminicial,kmfinal,valorgasolina,quantidade)
