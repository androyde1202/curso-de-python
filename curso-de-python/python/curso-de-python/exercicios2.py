#execicio1 retirar "#" para testes co exeção das linhas 1,10 e 18
#nome=input("qual o seu nome? ")
#ncarro= input("qual carro que você deseja? ")
#valorcar= float(input("qual é o valor desejado? "))
#cupons= float(input("qual é o valor do cupon que você tem? " ))
#valordodesconto= valorcar*(cupons/100)
#valorliquido= valorcar-valordodesconto
#print ("ok senhor(ra)", nome, "então você quer um(a)",ncarro, "?")
#print("então fica ",valorcar,"e com",cupons, "% de desconto fica", valorliquido)
# exercicio2
#nomedofunc=input("identificação:")
#dias= int (input("quantos dias de 24h você trabalhou:" ))
#horas=int(input("quantas horas de sobra você trabalhou:"))
#min=int(input("quantos minutos você trabalhou:"))
#seg=int(input("quantos segundos você trabalhou:"))
#segtotal=(seg+(min*60)+(horas*3600)+(dias*86400))
#print("você o funcionario ",nomedofunc, " trabalhou ", dias, " dias, ", horas, " horas, ",min," minutos e ",seg, " segundos totalizando então ", segtotal , " segundos")
#exercicio3
nomecli=input("qual o seu nome? ")
diasusados=float(input("quanto dias você utlizou o carro"))
kmrodado=float(input("quantos km você rodou com o carro?"))
diaria=float(input("qual o valor do aluguel da diaria"))
valorkm=float(input("qual o valor por km andado"))
total=((diasusados*diaria)+(kmrodado*valorkm))
print(" então senhor(ra) ", nomecli, "com" ,diasusados, "dias e " , kmrodado, "kms, com o preço de " , diaria, "por dia e com o preço de ", valorkm, "por km rodado o total da "
, total, "qual sera a forma de pagamento?")