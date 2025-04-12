#exercicio if1
#n1=int(input("numero"))
#n2=int(input("numero"))
#if n1>n2:
    #print(n1)
#else:
   # print(n2)
#exercicio if2
#salariovelho=float(input(" quanto você ganha por mês? "))
#if salariovelho>12500:
    #salarionovo=((salariovelho*0.1)+salariovelho)
   # print("com base no aumento de 10% seu novo salario sera:" ,salarionovo)
#else:
    #salarionovo=((salariovelho*0.15)+salariovelho)
    #print("com base no aumento de 15% seu novo salario sera:" ,salarionovo)
#exercicio 3 if elif else
idade=int(input("qual a sua idade? " ))
if idade<12:
    print("você é uma criança")
elif 12<=idade<18:
    print("você é um adolecente")
elif 18<=idade<60:
    print("você é um adulto")
else:
    print("você é um idoso")