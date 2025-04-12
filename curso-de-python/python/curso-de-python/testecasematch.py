diasdasemana=str(input("digite o dia da semana: "))
match diasdasemana: 
    case "segunda":
        print("fazer relatorio")
    case "terça":
        print("reunião")
    case "qunta":
        print("visitar cliente")
    case other:
        print("pode ir para a praia")