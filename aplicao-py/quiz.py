from connectdb import *

print("Quiz sobre a história das copas")

acertos = 0;
erros = 0;
condicao = 1
while condicao == 1:
    nome = input("Qual seu nome?: ")
    print("Olá", nome, "testar seu conhecimento sobre copas do mundo!")

    pergunta1 = int(input("1)Onde vai ser a próxima copa?\n1: Brasil\n2: Italia\n3: Marrocos\n4: Catar\n5: EUA\nResposta:"))
    if pergunta1 == 4:
        acertos+=1
    else:
        erros+=1

    pergunta2 = int(input("2)Qual seleção foi a última campeã?\n1: França\n2: Italia\n3: Brasil\n4: Alemanha\n5: Argentina\nResposta:"))
    if pergunta2 == 1:
        acertos+=1
    else:
        erros+=1
    
    pergunta3 = int(input("3)Qual foi o primeiro campeão?\n1: Holanda\n2: Italia\n3: Chile\n4: Uruguai\n5: Alemanha\nResposta:"))
    if pergunta3 == 4:
        acertos+=1
    else:
        erros+=1
    pergunta4 = int(input("4)Em quais anos aconteceram as copas do mundo no Brasil?\n1: 2014 e 1954\n2: 1962 e 2014\n3: 2014 e 1950\n4: 1982 e 2014\n5: 2014 e 1946\nResposta:"))
    if pergunta4 == 3:
        acertos+=1
    else:
        erros+=1
    pergunta5 = int(input("5)Quantas vezes o Brasil foi vice-campeão?\n1: 0\n2: 3\n3: 2\n4: 5\n5: 1\nResposta:"))
    if pergunta5 == 3:
        acertos+=1
    else:
        erros+=1
    pergunta6 = int(input("6)Qual o maior finalista?\n1: Brasil\n2: Italia\n3: França\n4: Argentina\n5: Alemanha\nResposta:"))
    if pergunta6 == 5:
        acertos+=1
    else:
        erros+=1
    pergunta7 = int(input("7)Quando e onde foi sediada a primeira copa?\n1: Brasil 1934\n2: Italia 1930\n3: Inglaterra 1934\n4: Uruguai 1930\n5: Inglaterra 1930\nResposta:"))
    if pergunta7 == 4:
        acertos+=1
    else:
        erros+=1
    pergunta8 = int(input("8)Qual dessas seleções foi duas vezes vice-campeã perdendo para o Brasil?\n1: Uruguai\n2: Italia\n3: Alemanha\n4: França\n5: Espanha\nResposta:"))
    if pergunta8 == 2:
        acertos+=1
    else:
        erros+=1
    pergunta9 = int(input("9)Em qual desses paises o Brasil conquistou o TRI-Campeonato?\n1: Mexico\n2: EUA\n3: Chile\n4: Japão\n5: Suécia\nResposta:"))
    if pergunta9 == 1:
        acertos+=1
    else:
        erros+=1
    pergunta10 = int(input("10)Quantas copas o Pelé jogou e ganhou?\n1: Jogou 5 e Ganhou 2\n2: Jogou 3 e Ganhou 3\n3: Jogou 4 e Ganhou 4\n4: Jogou 2 e Ganhou 2\n5: Jogou 4 e Ganhou 3\nResposta:"))
    if pergunta10 == 5:
        acertos+=1
    else:
        erros+=1
    pergunta11 = int(input("11)Quais dessas seleções são bi-campeãns?\n1: Holanda, Argentina, Uruguai\n2: Argentina, França, Uruguai\n3: Inglaterra, Argentina, França\n4: Holanda, Espanha, Inglaterra\n5: Argentina, França, Espanha\nResposta:"))
    if pergunta11 == 2:
        acertos+=1
    else:
        erros+=1    

    print(nome,"você Acertou:",acertos,"Errou:",erros)

    insert_db(nome, acertos, erros)

    acertos = 0
    erros = 0
    condicao  = int(input("Para jogar novamente aperte 1. Para parar aperte 2:\n"))
