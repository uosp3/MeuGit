import math
import random
#import pygame #pip3 install pygame
import urllib
import urllib.request
import time
import datetime
from operator import itemgetter #para ordernar um dicionario

cores = {'limpo': '\033[m',
         'amarelo': '\033[1;33m',
         'verde': '\033[1;32m',
         'azul' : '\033[34m',
         'vermelho': '\033[1;31m'}

desafio = int(input("informe o número do desafio a ser exibido: "))

match desafio:     
    case 5:
        #Desafio 5 = gerar um numero e mostrar seu sucessor e seu antecessor
        n=int(input("Didite um número: "))        
        print("O sucessor de {}{}{} é {} e o antecessor é {}".format(cores["amarelo"],n, cores["limpo"],(n+1),(n-1)))
       
    case 6:
        #Desafio 6 = mostrar o dobro o tripo e a raiz quadrada
        n=int(input("Digite um número: "))      
        print("O dobro de {} e {}, o triplo é {} e a raiz quadrada é {}".format(n, (n*2), (n*3), (n**(1/2))))

    case 7:
        #Desafio 7 = Ler duas notas e fazer a média
        nota1=float(input("Digide a primeira nota: "))
        nota2=float(input("Digide a segunda nota: "))
        print("A média das notas é {:.1f}".format((nota1+nota2)/2))

    case 8:
        #Desafio 8 = Converter metros para centimetros e milímetros
        metros=int(input("Informe quantos metros deseja fazer a conversão: "))
        print("{} metros equivalem a {} centímetros e a {} milímetros".format(metros,metros*100,metros*1000))

    case 9:
        #Desafio 9 = Nostrar a taboada de um número inteiro qualquer
        tab=int(input("Informe um número para vez a taboada do mesmo: "))
        i=1
        print("-"*12)#so para enfeitar
        while i<11:
            #resultado = tab*i
            print("{} x {:2} = {:2}".format(tab,i, tab*i))
            i=i+1
        print("-"*12)

    case 10:
        #Desafiop 10 - Converter real para dolar
        real=float(input("Informe quantos reais {}(R$){} voce tem para fazer a conversão para dolar (US$): ".format(cores["verde"],cores["limpo"])))
        #contacao=3.27
        print("Os seus R${:.2f} equivalem a US${:.2f}".format(real,real/3.27))

    case 11:
        #Desafio 11 = Ler largura e altura da parede, mostrar a àrea e a quantidade de tinta para pinta-la, sendo que cada litro de tinta pinta 2m quadrados
        largura=float(input("Digite a largura da parede, em metros: "))
        altura=float(input("Digite a altura da parede, em metros: "))
        print("A area total da parede é {:.2f} metros quadrados e serão necessários {:.2f} litros de tinta para pinta-la".format(largura*altura,(largura*altura)/2))

    case 12:
        #Desafio 12 - Infomar o preço de um produto e mostrar seu valor de venda com 5% de desconto
        preco=float(input("Informe o preço do produto, em reais R$: "))
        print("O valor final do produto com 5% desconto é R${:.2f} reais".format(preco*.95))
        
    case 13:
        #Desafio 13 - Informar o salário e mostrar o novo valor com um aumento de 15%
        salario=float(input("Digite o valor atual do salário R$: "))
        print("Após reajuste de 15% o novo salário será de R${:.2f}".format(salario*1.15))

    case 14:
        #Desafio 14 - Converter graus celcius para fahrenheit
        graus=float(input("Digite a temperatur em graus celcius para converter para fahrenheit: "))
        print("A temperatura de {:.1f}ºC corresponde a {:.1f}ºF".format(graus,(9*graus)/5+32))

    case 15:
        #Desafio 15 - Informar a quantidade km rodados por um carro alugado e quantos dias foram alugados. Calcular vr a pagar se o carro custa R$60 por dia e R$0.15 por km
        dias = int(input("Quantos dias o carro foi usado no aluguel? "))
        km = float(input("Quantos km foram rodados? "))
        print("O total a pagar é de R${:.2f}".format(km*.15+dias*60))

    case 16:
        #Desafio 16 - Ler um número real qualquer pelo teclado e mostre sua porção inteira
        nummero=float(input("Digite um número real: "))        
        print("O número digitado foi {} a parte inteira é {}".format(nummero, math.trunc(nummero)))
        print("O número digitado foi {} a parte inteira é {}".format(nummero, int(nummero)))
        print("O número digitado foi {} a parte inteira é {}".format(nummero, nummero//1))

    case 17:
        #Desafio 17 - Informar os catetos de um triângulo retângulo e mostrar o comprimento da hipotenusa
        catetoOposto=float(input("Infome o valor do cateto oposto: "))
        catetoAdjacente=float(input("Infome o valor do cateto adjacente: "))
        hip=(catetoOposto**2+catetoAdjacente**2)**.5
        hip2=math.hypot(catetoAdjacente,catetoOposto) #outra opção
        print("O comprimento da hipotenusa é {:.2f}".format(hip))
        print("O comprimento da hipotenusa é {:.2f}".format(hip2))

    case 18:
        #Desafio 18 - Informar o valor de um ângulo e mostrar o seno, cosseno e tangente desse ângulo
        angulo=float(input("Informe o valor do ângulo: "))
        radiano=math.radians(angulo)
        seno=math.sin(radiano)
        cosseno=math.cos(radiano)
        tan=math.tan(radiano)
        print("O cosseno do ângulo de {} graus é {:.2f}, o seno é {:.2f} e a tangente é {:.2f} e ele equivale a {:.2f} radianos".format(angulo,cosseno,seno,tan,radiano))

    case 19:
        #Desafio 19 - Sortear um dos 4 alunos para apagar o quadro. Ler o nome do aluno e imprimir
        aluno1=input("Primeiro aluno? ")
        aluno2=input("Segundo aluno? ")
        aluno3=input("Terceiro aluno? ")
        aluno4=input("Quarto aluno? ")
        lista=[aluno1,aluno2,aluno3,aluno4]
        sorteado = random.choice(lista) #escolhe um da lista
        print("O aluno sorteado foi {}".format(sorteado))

    case 20:
        #Desafio 20 - Sortear a ordem de apresentação dos trabalhos de quatro alunos
        aluno1=input("Primeiro aluno? ")
        aluno2=input("Segundo aluno? ")
        aluno3=input("Terceiro aluno? ")
        aluno4=input("Quarto aluno? ")
        lista=[aluno1,aluno2,aluno3,aluno4]
        random.shuffle(lista) #embaralha a lista
        print("A orde de apresentação será {}".format(lista))

    case 21:
        #Desafio 21 - Tocar mp3
        pygame.init()
        pygame.mixer.music.load("E:\\Music\\Richard Clayderman - 29\\Richard Clayderman-CHARIOTS OF FIRE.mp3")#caminho do arquivo mp3
        pygame.mixer.music.play()
        input()
        pygame.event.wait()

    case 22:
        print
        #Desafio 22 - Ler o nome completo de uma pessoa e mostrar
        #Passar o texto para maiúsculo
        #Passar o texto para minúsculo
        #Quantas letras ao todo, sem considerar espaços
        #Qual o primeiro nome e quantas letras ele tem.
        nome=str(input("Digite seu nome completo: ")).strip()
        print("Analisando seu nome...\nSeu nome em maíusculas: {}".format(nome.upper()))
        print("Seu nome em minúsculas: {}".format(nome.lower()))
        print("Seu nome tem {} letras".format(len(nome)-nome.count(" ")))  
        separa=nome.split()      
        print("O seu primeiro nome é {} e ele tem {} letras".format(separa[0],len(separa[0])))
    case 23:
        #Desafio 23 - Ler um número de 0 a 9999 e mostrar cada dígito separado.
        #Exemplo 1834, 4 unidades, 3 dezenas, 8 centenas e 1 milhar
        numero=int(input("Digite um númro de 0 a 9999: "))
        u = numero//1%10 #faz uma divisão para obter parte inteira e  depois pega o módulo da divisão por 10
        d = numero//10%10
        c = numero//100%10
        m = numero//1000%10        
        print("O numero {}, tem {} unidade(s), {} dezena(s), {} centena(s) e {} milhar(es)".format(numero, u, d, c, m))

    case 24:
        #Desafio  24 - Ler o nome de uma cidade e dizer se ela começão ou não com "SANTO"
        cidade=input("Em que cidade voce nasceu? ").strip().upper()
        print(cidade[:5]=="SANTO")#retorna True ou False

    case 25:        
        #Desafio 25 - Ler o nome de uma pessoa e dizer se ela tem "SILVA" no nome
        nome=input("Qual o seu nome completo? ").strip().upper()
        print("Voce é da familia Silva? {}".format("SILVA" in nome))   #retorna True ou False

    case 26:
        #Desafio 26 - Ler uma frase e mostrar quantas letras 'a' aparece, em que posição aparece o primeiro 'a'e em que posição aparece a última vez
        frase=input("Digite uma frase: ").strip().upper()
        print("A letra A aparece {} vezes na frase.".format(frase.count("A")))
        print("A primeira letra A apareceu na posição {}".format(frase.find("A")+1))
        print("A última letra A apareceu na posição {}".format(frase.rfind("A")+1))
    
    case 27:
        #Desafio 27 - Ler o nome completo de uma pessoa e mostrar o primeiro e o último nome, separadamente.
        nome=input("Digite o nome completro de uma pessoa ").strip()
        nome=nome.split()
        tam=len(nome)
        print("Primeiro nome é {} e o último nome é {}".format(nome[0], nome[-1]))

    case 28:
        #Desafio 28 - Gerar um número aleatório entre 0 e 5 e tentar descobrir o número gerado pelo computador. Imprimir certo ou errado.
        print("-=-"*20)
        print("Vou pensar em um numero entre 0 e 5. Tente adivinhar...")
        print("-=-"*20)
        computador=random.randint(0,5)
        jogador=int(input("Em que número eu pensei? "))
        print("Processando...")
        time.sleep(3)
        if computador==jogador:
            print("PARABENS! Você conseguiu me vencer")
        else:
            print("GANHEI! Eu pensei no número {} e não no {}! ".format(computador,jogador))

    case 29:
        #Desafio 29 - Ler a velociade de um carro e se ultrapassar 80km/h mostrar mensagem dizendo que foi multado qual o valor da multa, sendo que a multa é de R$7,00 para cada km acima do limite.
        velocidade=float(input("Qual a velocidade atual do carro? "))
        if velocidade>80:
            multa=(velocidade-80)*7
            print("MULTADO! Você excedeu o limite permitido que é de 80km/h \nVocê deve pagar uma multa de R${:.2f} ".format(multa))
        print("Tenha um bom dia! Dirija com segurança!")

    case 30:
        #Desafio 30 - Ler um numero inteiro e dizer se é par ou impar
        n=int(input("Digite um número qualquer: "))
        resto= n%2
        if resto == 0:
            print("O numero {} é PAR".format(n))
        else:
            print("O número {} é IMPAR".format(n))

    case 31:
        #Desafio 31 - Ler a distancia de uma viagem em km e calcular o preço da passagem, cobrando R$0.50 por km para viagem até 200km e cobrar R$0.45 para viagens acima de 200km
        distancia=float(input("Qual a distância da sua viagem? "))
        print("Voce está preste a começar uma viagem de {:.1f}kn".format(distancia))
        if distancia<=200:
            preco=distancia*.5
        else:
            preco=distancia*.45
        print("O preço da sua passagem será de R${:.2f}".format(preco))

    case 32:
        #Desafio 32 - Ler um ano qualquer e dizer se é ou não bissexto
        #import datetime
        ano=int(input("Que ano quer analisar? Coloque 0 para analisar o ano atual: "))
        if ano == 0:
            ano = datetime.date.today().year
        if ano % 4 == 0 and ano % 100 !=0 or ano % 400 == 0:
            print("O ano {} é bissexto".format(ano))
        else:
            print("O ano {} não é bissexto".format(ano))


    case 33:
        #Desafio 33 - Ler 3 numeros e informar qual o maior e qual o menor
        print(cores["vermelho"])
        n1=int(input("Primeiro valor: "))
        n2=int(input("Segundo valor: "))
        n3=int(input("Terceiro valor: "))
        print(cores["limpo"])
        menor=n1 #partindo de pre suposto que n1 é o menor
        if n2<n1 and n2<n3:
            menor=n2
        if n3<n1 and n3<n2:
            menor=n3
        maior=n1 #partindo do pre suposto que n1 é o maior
        if n2>n1 and n2>n3:
            maior=n2
        if n3>n1 and n3>n2:
            maior=n3
        print("O menor valor digitado foi {}".format(menor))
        print("O maior valor digitado foi {}".format(maior))

    case 34:
        #Desafio 34 - Ler o valor de um salário e calcular o aumento, sendo 10% para salário acima de R$1.250,00 e de 15% para salários abaixo desse valor.
        salario=float(input("Qual é o salário do funcionário? R$"))
        if salario <= 1250:
            novo= salario*1.15
        else:
            novo= salario*1.1
        print("Quem ganhava {}R${:.2f}{} agora passa a ganhar R${:.2f}".format(cores["azul"],salario,cores["limpo"],novo))

    case 35:
        #Desafio 35 - Ler 3 comprimentos de retas e dizer se com elas é possível formar um triângulo.
        print("-=-"*10)
        print("Analisador de Triângulos")
        print("-=-"*10)
        s1=float(input("Primeiro segmento do triângulo: "))
        s2=float(input("Segundo segmento do triângulo: "))
        s3=float(input("Terceiro segmento do triângulo: "))        
        if s1< (s2 + s3) and s2< (s1 + s3) and s3< (s2 + s1):
            print("Os segmentos digitados PODEM FORMAR triângulo!")
        else:
            print("Os segmentos digitados NÃO PODEM FORMAR triângulo!")

    case 36:
        #Desafio 36 - Aprovar um empréstimo para compra de uma casa. Perguntar o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
        #Calcule o valor da prestação mensal sabendo que ela não pode exceder 30% do salário.
        valorCasa=float(input("Qual o valor da casa que deseja comprar? R$ "))
        salario=float(input("Qual o seu salário? R$ "))
        tempo=int(input("Em quantos anos deseja quitar o emppréstimo: "))
        prestacao=valorCasa/(tempo*12)
        percent=(prestacao/salario)*100
        if percent>30:
            print("Infelizmente voce não poderá fazer o financimento. A valor da prestação (R${:.2f}) compromente {:.2f}% do seu salário, o limite permitido é de até 30% da sua renda".format(prestacao,percent))
        else:
            print("Seu financiamento foi aprovado, voce pagará em {} meses, uma prestação de R${:.2f}, isto corresponde a {:.2f}% da sua renda".format(tempo*12, prestacao,percent))

    case 37:
        #Desafio 37 - Ler um número inteiro, qualquer, e escolher a base de conversão: Binário, Octal ou Hexadecimal.
        n=int(input("Digite um número inteiro: "))
        print("Escolha uma das bases para conversão: ")
        print("[1] converter para BINÁRIO: ")
        print("[2] converter para OCTAL: ")
        print("[3] converter para HEXADECIMAL: ")
        opcao=int(input("Sua opção: "))
        
        if opcao == 1:
            base="BINÁRIO"
            convertido = bin(n)[2:]
        elif opcao == 2:
            base="OCTAL"
            convertido= oct(n)[2:]
        elif opcao ==3:
            base="HEXADECIMAL"
            convertido= hex(n)[2:]
        else:
            base="INVÁLIDA"

        if base!="INVÁLIDA":   
            print("{} convertido para {} é igual a {}".format(n,base,convertido))
        else:
            print("Opção inválida")


    case 38:
        #Desafio 38 - Ler dois números inteiros e comparar mostrando qual é o maior ou se são iguais.
        p=int(input("Primeiro número: "))
        s=int(input("Segundo número: "))
        if p>s:
            print("O PRIMEIRO valor é maior")
        elif p<s:
            print("O SEGUNDO valor é maior")
        else:
            print("Os dois valores são IGUAIS")

    case 39:
        #Desafio 39 - Ler o ano de nascimento e informar se ainda vai se alistar, se ja é hora de se alistar ou se ja passou do tempo do alistamento. Mostrar o tempo que falta ou que passou do prazo.
        ano=int(input("Ano de nascimento: "))
        idade = datetime.date.today().year - ano
        print("Quem nasceu em {} tem {} em {}".format(ano,idade,datetime.date.today().year))
        if idade < 18:
            print("Ainda falta(m) {} ano(s) para o alistamento".format(18-idade))
            print("Seu alistamento será em {}".format(18-idade+datetime.date.today().year))
        elif idade >18:
            print("Voce ja deveria ter se alistado ha {} anos".format(idade-18))
            print("Seu alistamento foi em {}".format(datetime.date.today().year-idade+18))
        else:
            print("Você tem que se alista IMEDIATAMENTE!")

    case 40:
        #Desafio 40 - Ler duas notas de aluno, calcular a média e mostrar, de acordo com a média, abaixo de 5 reprovado, entre 5 e 6.9 recuperação e de 7 acima aprovado.
        n1=float(input("Primeira nota: "))
        n2=float(input("Segunda nota: "))
        media=(n1+n2)/2
        print("Tirando {} e {} a média do aluno é {:.2f}".format(n1,n2,media))
        if media < 5:
            print("O aluno está REPROVADO")
        elif media >=7:
            print("O aluno está APROVADO")
        else:
            print("O aluno está em RECUPERAÇÃO")  
   

    case 41:
        #Desafio 41 - Ler o ano de nascimento e mostrar a categoria, para natação, de acordo com a idade
        #Até 9 anos: Mirim
        #Até 14 anos: Infantil
        #Até 19 anos: Junior
        #Até 25 anos: Senior
        #Acima: Master.
        ano=int(input("Ano de Nascimeto: "))
        idade = datetime.date.today().year-ano
        print("O atleta tem {} anos.".format(idade))
        if idade <= 9:
            print("Classificção MIRIM")
        elif idade <= 14:
            print("Classificação INFANTIL")
        elif idade <= 19:
            print("Classificação JUNIOR")
        elif idade <= 25:
            print("Classificação SENIOR")
        else:
            print("Classificação MASTER")

    case 42:
        #Desafio 42 - Refaça o desafio 35 e diga se, caso seja possível formar o triângulo, o triângulo é Equilátero (3 lados iguais), Isósceles (2 lados iguais) ou Escaleno (todos os lados diferentes)
        print("-=-"*10)
        print("Analisador de Triângulos")
        print("-=-"*10)
        s1=float(input("Primeiro segmento do triângulo: "))
        s2=float(input("Segundo segmento do triângulo: "))
        s3=float(input("Terceiro segmento do triângulo: ")) 

        if s1< (s2 + s3) and s2< (s1 + s3) and s3< (s2 + s1):
            if s1 == s2 == s3:
                tipo = "Equilátero"
            elif s1 != s2 !=s3 != s1:
                tipo = "Escaleno"
            else:
                tipo = "Isosceles"

            print("Os segmentos digitados PODEM FORMAR triângulo do tipo {}!".format(tipo))
        else:
            print("Os segmentos digitados NÃO PODEM FORMAR triângulo!")

    case 43:
        #Desafio 43 - Ler o peso e altura, calcular o IMC e mostrar o status
        # Abaixo de 18.5: abaixo do peso
        # Entre 18.5 e 25: peso ideal
        # Entre 25 e 30: sobrepeso
        # Entre 30 e 40: Obesidade
        # Acima de 40: Obesidade mórbida
        peso=float(input("Qual é seu peso? (kg) "))
        altura=float(input("Qual é sua altura? (m) "))
        imc= peso/(altura**2)
        print("O IMC dessa pessoa é de {:.2f}".format(imc))
        if imc < 18.5:
            print("Voce está na abaixo do peso ideal")
        elif imc < 25:
            print("Parabéns, você está na faixa de peso ideal")
        elif imc <30:
            print("Voce está com sobrepeso")
        elif imc < 40:
            print("Você está obeso")
        else:
            print("Voce está com obesidade mórbida")

    case 44:
        #Desafio 44 - Calcular o valor a ser pago por um produto, considerando o seu preço normal e condiçãode pagamento:
        # À vista (Dinheiro/Cheque): 10% de desconto
        # À vista (cartão): 5% de desconto
        # Até 2x (cartão): preço normal
        # 3x ou mais (cartão): 20% de juros.
        print("{:=^40}".format(" LOJAS GOMES "))
        compra=float(input("Preço das compras: R$ "))
        print("""Formas de pagamento
        [1] á vista dinheiro/cheque
        [2] à vista cartão
        [3] 2x no cartão
        [4] 3x ou mais no cartão """)
        opcao=int(input("Sua opção: "))

        if opcao == 1:
            print("Sua compra de R${:.2f} vai custar R${:.2f} no final".format(compra,compra*.9))
        elif opcao == 2:
            print("Sua compra de R${:.2f} vai custar R${:.2f} no final".format(compra,compra*.95))
        elif opcao == 3:
            print("Sua compra de R${} será parcelada em 2x de {:.2f}, não terá desconto nem juros".format(compra,compra/2))
        elif opcao ==4:
            parcelas=int(input("Quantas parcelas? "))
            vr_parcela = (compra*1.2/parcelas)
            print("Sua compra será parcelada em {}x de R${:.2f} com juros".format(parcelas,vr_parcela))
            print("Sua compra de R${:.2f} vai custar R${:.2f} no final".format(compra,compra*1.2))            
        else:
            print("Opção inválida")

    case 45:
        #Desafio 45 - Jogar jokenpô(pedra, papel, tesoura) com o computador.
        itens=["PEDRA", "PAPEL", "TESOURA"]
        print("Suas opções: ")
        print("[0] PEDRA")
        print("[1] PAPEL")
        print("[2] TESOURA")
        jogador=int(input("Qual é a sua jogada? "))
        computador=random.randint(0,2)

        print("JO")
        time.sleep(1)
        print("KEN")
        time.sleep(1)
        print("PO!!!")
        time.sleep(1)
        print("-=-"*10)
        print("Computador jogou {}".format(itens[computador]))
        print("Jogador jogou {}".format(itens[jogador]))
        print("-=-"*10)
        if computador == 0: #pedra
            if jogador == 0:
                print("EMPATE")
            elif jogador == 1:
                print("JOGADOR VENCE")
            elif jogador ==2:
                print("COMPUTADOR VENCE")
            else:
                print("Jogada inválida!")

        elif computador == 1: #papel
            if jogador == 0:
                print("COMPUTADOR VENCE")
            elif jogador == 1:
                print("EMPATE")
            elif jogador ==2:
                print("JOGADOR VENCE")
            else:
                print("Jogada inválida!")

        elif computador == 2: #tesoura
            if jogador == 0:
                print("JOGADOR VENCE")
            elif jogador == 1:
                print("COMPUTADOR VENCE")
            elif jogador ==2:
                print("EMPATE")
            else:
                print("Jogada inválida!")

    case 46:
        #Desafio 46 - Mostrar uma contagem regressiva indo de 10 até 0 com pausa de 1 segundo entre eles.
        for c in range(10,-1,-1):
            print(c)
            time.sleep(1)
        print("BUM! BUM! POOW!")

    case 47:
        #Desafio 47 - Mostrar todos os números pares entre 1 e 50
        for c in range(2,51,2):
            print(c,end=' ')
        print("Acabou...")

    case 48:
        #Desafio 48 - Calcular a soma entre todos os números IMPARES que são MÚLTIPLOS DE TRES, no intervalo de 1 a 500
        soma=0
        contador=0
        for c in range(1,500,2):
            if c%3 == 0:
                soma+=c
                contador+=1
        print("A soma de todos os {} valores solicitados é {}".format(contador,soma))


    case 49:
        #Desafio 49 - Refaça o desafio 09 com o laço FOR.
        tab=int(input("Informe um número para vez a tabuada do mesmo: "))        
        print("-"*12)#so para enfeitar
        for c in range(1,11):
            print("{}  X {:2} = {:2}".format(tab,c,tab*c))# os :2 é para escrever com dois dígitos, ou espaços antes
        print("-"*12)

    case 50:
        #Desafio 50 - Ler 6 números inteiros e mostrar a soma apenas dos que forem PAR.
        soma=0
        cont=0
        for c in range(1,7):
            n=int(input("Digite o {}º número: ".format(c)))
            if n%2==0:
                soma+=n
                cont+=1
        print("Você informou {} número(s) PAR(ES) e a soma foi :{}".format(cont,soma))

    case 51:
        #Desafio 51 - Ler o primeiro termo e a razão de uma PA. No final mostrar os 10 primeiros termos dessa PA
        print("="*30)
        print("{}10 TERMOS DE UMA PA{}".format(" "*6," "*6))
        print("="*30)
        pt=int(input("Primeiro termo: "))
        r=int(input("Razão: " ))
        decimo = pt+ (10-1)*r
        for c in range(pt,decimo+r,r):
            print("{}".format(c),end=" -> ")
        print("Acabou...")

    case 52:
        #Desafio 52 - Ler um número inteiro e dizer se ele é PRIMO
        n=int(input("Digite um númro: "))
        contador=0
        for c in range(1,n+1):            
            if n%c==0:
                contador=contador+1
                print("\033[33m",end="")
            else:
                print("\033[31m",end="")
            print("{} ".format(c),end="")
        print("\n\033[m O número {} foi divisível {} vezes".format(n,contador))
        if contador==2:
            print("E por isto ele É PRIMO")
        else:
            print("E por isto ele  NÃO É PRIMO")

    case 53:
        #Desafio 53 - Ler uma frase qualquer e diga se ela é um PALÍNDROMO, desconsiderando os espaços. Palindromo é a palavra/texto que lido de tras pra frente é a mesma coisa
        frase=str(input("Digite uma frase: ")).upper()
        frase=frase.replace(" ","")#tira os espaços      
        inverso=""
        #o for, abaixo pode ser substituido por: inverso = frase[::-1] -> começa no inicio, termina no fim, de tras pra frente.
        for letra in range(len(frase)-1,-1,-1):
            inverso+=frase[letra]
        print("O inverso de {} é {}".format(frase,inverso))
        if inverso== frase:
            print("Temos um palíndromo")
        else:
            print("Não temos um palíndromo")
           

    case 54:
        #Desafio 54 - Ler o ano de nascimento de 7 pessoas. No final mostrar quantas ja são maiores de 21 e quantas não são.
        atual=datetime.date.today().year
        menores=maiores=0
        for c in range(1,8):
            nasc = int(input("Em que ano a {}ª pessoa nasceu? ".format(c)))
            idade=atual-nasc
            if idade < 21:
                menores+=1
            else:
                maiores+=1        
        print("Ao todo tivemos {} pessoas maiores de idade".format(maiores))
        print("E também tivemos {} pessoas menores de idade".format(menores))
    case 55:
        #Desafio 55 - Ler o peso de 5 pessoas. No final mostre qual foi o maior e o menor.
        for c in range(1,6):
            peso=float(input("Peso da {}ª pessoa: ".format(c)))
            if c==1:
                maior=peso
                menor=peso
            else:
                if peso>maior:
                    maior=peso
                if peso<menor:
                    menor=peso            
        print("O maior pelo lido foi de {}kg".format(maior))
        print("O menor pelo lido foi de {}kg".format(menor))

    case 56:
        #Desaio 56 - Ler o nome, idade e sexo de 4 pessoas. No final mostrar:
        # A média de idade do grupo
        # O nome do homem mais velho
        # Quantas mulheres tem menos de 20 anos
        somaidade=0
        idadevelho=0
        novinha=0
        for c in range(1,5):
            print("-----{}ª PESSOA-----".format(c))
            nome=str(input("Nome......: "))
            idade=float(input("Idade.....: "))
            sexo=str(input("Sexo [M/F]: ")).upper()
            somaidade+=idade
            if sexo=="M" and idade > idadevelho: #pode ser usado: if sexo in "Mm" and ...
                homemvelho=nome
                idadevelho=idade
            if sexo=="F" and idade<20: #pode ser usado: if sexo in "Ff" and ...
                novinha+=1
        print("A média de idade do grupo é de {} anos".format(somaidade/4))
        print("O homem mais velho é {}, com {} anos de idade.".format(homemvelho,int(idadevelho)))
        print("Ao todo é(são) {} mulher(es) com menos de 20 anos".format(novinha))

    case 57:
        #Desafio 57 - Ler o sexo de uma pessoa, mas so aceitar os valores M ou F. Caso contrário peça a digitação novamente.
        sexo=str(input("Informe seu sexo: [M/F] ")).upper().strip()
        while sexo != "M" and sexo != "F":
            sexo=str(input("Dados inválidos. Por favor, informe seu sexo: [M/F] ")).upper().strip()
        print("Sexo {} registrado com sucesso.".format(sexo))

    case 58:
        #Desafio 58 - Melhorar o jogo do desafio 28, o computador vai sortear um número entre 0 e 10. Agora, o jogador vai tentar advinhar até acertar, mostrar no final quantas tentativas foram feitas até acetar.
        print("-=-"*23)
        print("Sou seu computador...\nAcabei de pensar em um numero entre 0 e 10. Tente adivinhar...")
        print("-=-"*23)
        computador=random.randint(0,10)
        jogador=int(input("Em que número eu pensei?\033[1;33m"))        
        print("\033[mProcessando...")
        time.sleep(1.5)
        tentativa=1
        while computador != jogador:
            tentativa+=1
            if computador - jogador > 0:
                jogador=int(input("\033[mMais... Tente outra vez.\nQual é seu palpite?  \033[1;33m"))
            else:
                jogador=int(input("\033[mMenos... Tente outra vez.\nQual é seu palpite? \033[1;33m"))
        print("\033[mParabens, voce acertou com de \033[1;33m{}\033[m tentativa(s).".format(tentativa))

    case 59:
        #Desafio 59 - Ler 2 números, depois mostrar as opções (menu):
        #1 - somar
        #2 - multiplicar
        #3 - maior
        #4 - novos números
        #5 - sair
        # Fazer as operçãoes solicitadas no menu.
        n1=int(input("Primeiro valor: "))
        n2=int(input("Segundo valor: "))
        sair=False
        while not sair:
            print("[1] Somar")
            print("[2] Multiplicar")
            print("[3] Maior")
            print("[4] Tentar outros números")
            print("[5] Sair do programa")
            opcao=int(input(">>>>> Qual sua opção? "))
            if opcao==1:
                soma=n1+n2
                print("\033[1;33mA soma entre {} + {} é {}\033[m".format(n1,n2,soma))
            elif opcao ==2:
                multiplicacao=n1*n2
                print("\033[1;33mA multiplicação  entre {} x {} é {}\033[m".format(n1,n2,multiplicacao))
            elif opcao==3:                
                maior=[n1,n2] 
                maior=max(maior,key=int)
                print("\033[1;33mO maior valor entre {} e {} é {}\033[m".format(n1,n2,maior))
            elif opcao==4:
                n1=int(input("Primeiro valor: "))
                n2=int(input("Segundo valor: "))
            elif opcao==5:
                sair=True
            else:
                print("\033[1;33mOpção inválida, redigite!\033[m")
            print("-=-"*23)

    case 60:
        #Desafio 60 - Ler um número e mostrar o fatorial
        #Python tem uma função para isto, mas aqui é pra fazer com while.
        n=int(input("Digite um número para calcular seu fatoria: "))
        c=n
        f=1
        print("Calculando {}! =".format(n), end=" ")
        while c>0:
            print("{}".format(c), end=" ")
            print(" x " if c > 1 else " = ", end=" ")
            f*=c
            c -= 1
        print("{}".format(f))


    case 61:
        #Desafio 61 - Refaça o desafio 51 com while
        print("="*30)
        print("{}10 TERMOS DE UMA PA{}".format(" "*6," "*6))
        print("="*30)
        pt=int(input("Primeiro termo: "))
        r=int(input("Razão: " ))
        c=0
        termo=pt
        while c<10:
            print("{}".format(termo),end=" -> ")
            termo+=r
            c+=1        
        print("Acabou...")

    case 62:
        #Desafio 62 - Melhore o desafio 61, perguntando se quer mostrar mais alguns termos(S/N), ou 0 termos
        print("="*30)
        print("{}TERMOS DE UMA PA{}".format(" "*6," "*6))
        print("="*30)
        pt=int(input("Primeiro termo: "))
        r=int(input("Razão: " ))
        c=0
        termo=pt
        qtde=10
        while c<qtde:
            print("{}".format(termo),end=" -> ")
            termo+=r
            c+=1        
            if c==qtde:
                print("Pausa...")
                pt=termo+r
                maistermos=int(input("Quantos termos você quer mostrar a mais? "))
                if maistermos!=0:
                    qtde+=maistermos
        print("Progressão finalizada com {} temor mostrados.".format(qtde))

    case 63:
        #Desafio 63 - Ler um número inteiro e mostrar os n primeiros elementos de uma sequencia de Fibonacci. Ex.: 0 > 1 > 1 > 2 > 3 >5 > 8...
        print("="*30)
        print("{} Sequência de Fibonacci {}".format(" "*6," "*6))
        print("="*30)
        termos=int(input("Quantos termos voce quer mostrar? "))
        n=3
        print("0 -> 1", end=' -> ')
        penultimo=0
        ultimo=1
        while n <= termos:
           atual=penultimo+ultimo
           print(atual,end=' -> ')
           penultimo=ultimo
           ultimo=atual
           n+=1 
        print("Fim")

    case 64:
        #Desafio 64 - Ler vários números inteiros. O programa so para quando entrar 999. Mostrar quantos números foram digitados, a soma deles(desconsiderando o flag(999))
        n=q=s=0
        n=int(input("Digite um número [999 para parar]: "))
        while n!=999:
            s+=n
            q+=1
            n=int(input("Digite um número [999 para parar]: "))            
            
        print(f"Você digitou {q} números e a soma entre eles foi {s}")

    case 65:
        #Desafio 65 - Ler vários números inteiros. Mostrar a média, qual o maior e o menor. O prog deve perguntar se quer ou não continuar a dititação.
        sn="S"
        q=soma=maior=0
        while sn!="N":
            n=int(input("Digite um número: "))
            q+=1
            if q==1:
                maior=menor=n
            soma=soma+n
            if n>maior:
                maior=n
            if n<menor:
                menor=n
            sn=input("Quer continuar? [S/N] ").upper()
        print(f"Voce digitou {q} números e a média foi {soma/q}")
        print(f"O maior valor foi {maior} e o menor foi {menor}")

    case 66:
        #Desafio 66 - Ler vários números inteiros.So parar quando for 999.Mostrar quantos números foram digitados e qual a soma (sem o 999).
        q=s=0
        while True:
            n=int(input("Digite um número [999 para parar]: "))
            if n==999:
                break            
            s+=n
            q+=1
            
        print(f"Você digitou {q} números e a soma entre eles foi {s}")

    case 67:
        #Mostrar a tabuada de n numeros, um por vez, para cada n digitado. Interromper quan n for negativo
        while True:
            n=int(input("Quer ver a tabuada de qual valor? "))
            print("~"*30)
            if n<0:
                break
            for t in range(1,11):
                print(f'{n} x {t:2} = {n*t:2}')
            print("~"*30)
        print("Progama de tabuada encerrado. Volte sempre!")
        
    case 68:
        #Jogar par ou impar com o pc. O jogo para quando o jogador perder.Mostrar total de vitórias consecutivas que ele conquistou
        #Vamos jogar par ou impar
        print("=-"*30)
        print("VAMOS JOGAR PAR OU ÍMPAR")
        print("=-"*30)
        v=0
        while True:
            n=int(input("Diga um valor: "))   
            computador=random.randint(0,11)
            soma=n+computador
            pi=" "
            while pi not in "PpIi":
                pi=str(input("Voce quer PAR ou ÍMPAR? [P/I] ")).upper()
            if pi =="":
                print("Entrada inválida...")
                break
            escolha='PAR'
            if pi=="I":
                escolha = "IMPAR"
            r="PAR"            
            if soma%2==1:
                r="IMPAR"           
            print("-"*30)
            print(f"Você jogou {n} e o computador jogou {computador}. Total de {n+computador} DEU {r}")
            escore="Perdeu"
            if r==escolha:
                v+=1
                escore="Ganhou"
                print(f"Voce {escore}")
                print("Vamos jogar novamente...")
            else:
                print(f"GAME OVER! Você venceu {v} vez(es)")
                break
            print("-"*30)

    case 69:
        #Ler idade e sexo de n pessoas.Perguntar se quer continuar.
        #Mostrar quantos tem mais de 18 anos.
        #Quantos homens foram cadastrados
        #Quantas mulheres tem menos de 20 anos.
        # Assim:
        maior=homem=mulher_menor=0
        while True:
            print("CADASTRE UMA PESSOA")
            idade=int(input("Idade: "))
            sexo=" "
            while sexo not in "MF":
                sexo=str(input("Sexo: [M/F] ")).upper()
            if idade>=18:
                maior+=1
            if sexo=="M":
                homem+=1
            elif idade<20:
                mulher_menor+=1
            opcao=" "
            while opcao not in "SN":
                opcao=str(input("Quer continuar? [S/N] ")).upper()
            if opcao=="N":
                break
        print(f"Total de pessoas com mais de 18 anos: {maior}")
        print(f"Ao todo temos {homem} homem(ns) cadastrado(s)")
        print(f"E temos {mulher_menor} mulher(es) com menos de 20 anos")            
        
    case 70:
        #Ler o nome e o preço de n produtos. Continuar?
        #Mostrar:
                #Total gasto na compra
                #Quantos produtos custam mais de 1000
                #Qual o nome do produto mais barato.
        print("LOJA SUPER BARATÃO")
        soma=mais_de_mil=0
        mais_barato=" " 
        while True:
            produto=str(input("Nome do Produto: ")).upper()
            preco=int(input("Preço: R$"))
            if preco>1000:
                mais_de_mil+=1
            if soma==0 or preco<menor_preco:
                menor_preco=preco
                mais_barato=produto       
            soma+=preco                       
            opcao=" "
            while opcao not in "SN":
                opcao=str(input("Quer continuar? [S/N] ")).upper()
            if opcao=="N":
                break
        print(f"O total da compra foi R${soma:.2f}")
        print(f"Temos {mais_de_mil} produto(s) custando mais de R$1.000,00")
        print(f"o produto mais barato foi {mais_barato} que custa R${menor_preco:.2f}")

    case 71:
        #Simular o funcionamento de caixa eletrônico
        #Quanto será sacado?(int)
        #Informar quantas cédulas de cada vr.(50, 20, 10 e 1)
        print("BANCO CEV")
        valor=int(input("Que valor você quer sacar? R$"))
        total=valor
        ced = 50
        totced = 0
        while True:
            if total>=ced:
                total-=ced
                totced+=1
            else:
                if totced>0:
                    print(f"Total de {totced} cédulas de R${ced}")
                if ced==50:
                    ced=20
                elif ced ==20:
                    ced=10
                elif ced ==10:
                    ced=1
                totced=0
                if total==0:
                    break    
        print("Volte sempre ao BANCO CEV! Tenha um bom dia!") 

    case 72:
       pass
       #Ter uma tupla preenchida com uma contagem por extenso de zero até 20
       #Ler um número pelo teclado (0 a 20) e mostrar por extenso.
       #Se digitar fora da faixa: Tente novamente.Digite um número entre 0 e 20
       #exibir: Voce digitou o número xxxxxxx
       numeros= ("zero","um","dois","tres","quatro","cinco","seis","sete","oito","nove","dez","onze","doze","treze","catorze","quinze","dezesseis","dezessete","dezoito","dezenove","vinte")
       opcao=" "
       while True: 
            n=int(input("Digite um númro entre 0 e 20: "))
            if 0 <= n <=20:
                print(f"Voce digitou o número {numeros[n]}")
                while opcao not in "SN":
                    opcao= str(input("Quer continuar? [S/N]")).upper()
                if opcao=="N":
                    break
            opcao=" "

    case 73:
       pass
       #Tupla com os 20 times da série A (em ordem de classificação)
       times=("Palmeiras","Grêmio","Atletico/MG","Flamengo","Botafogo","Bragantino","Fluminense","Athletico","Internacional","Fortaleza","São Paulo","Cuiabá","Corinthians","Cruzeiro","Vasco","Bahia","Santos","Goiás","Coritiba","América/MG",)
       print("*-*"*35)
       print(f"Lista dos times do brasileirão/2023:")
       print(times)
       print("*-*"*35)
       #Mostrar os 5 primeiros       
       print("Os 5 primeiros são:")
       print(times[0:5])
       print("*-*"*35)
       #Mostrar os 4 últimos
       print("Os 4 últimos são:")
       print(times[-4:])
       print("*-*"*35)
       #Mostrar lista em ordem alfa
       print("Times em ordem alfabética:")
       print(sorted(times))
       #Mostrar a posição de um determinado time(Cruzeiro, por exemplo.)
       print(f"O Cruzeiro está na {times.index("Cruzeiro")+1}ª posição")

    case 74:  
       #Gerar 5 números aleatórios e colocar em uma tupla.      
       numeros=(random.randint(1,10),random.randint(1,10),random.randint(1,10),random.randint(1,10),random.randint(1,10))
       #Mostrar a listagem gerada
       print(f"Os valores sorteados foram {numeros}")             
       #Mostrar o menos e o maior.
       print(f"O maior valor sorteado foi {max(numeros)}")
       print(f"O menor valor sorteado foi {min(numeros)}")

    case 75:
       #Ler 4 valores pelo teclado e guardar em um tupla, no final mostrar:
        numeros=(int(input("Digite um número ")),int(input("Digite outro número ")),int(input("Digite mais um número ")),int(input("Digite o último número ")))
        print(f"Voce digitou os valores {numeros}")
       #Quantas vezes aparece o valor 9
        nove=numeros.count(9)
        if nove!=0:
            print(f"O valor 9 apareceu {nove} vez(s)")
        else:
            print("O valor nove não apareceu nenhuma vez")
       #Em qual posição aparece o primeiro 3
        if 3 in numeros:
            print(f"O valor 3 aparece na {numeros.index(3)+1}ª posição")
        else:
            print("O valor 3 não foi digitado em nenhuma posição.")
       #Quantos foram pares
        qt_par=0        
        for par in numeros:
            if par%2==0:
                qt_par+=1
                if qt_par==1:
                    print(f"Os números pares são: {par}",end=" ")
                else:
                    print(par,end=" ")
        if qt_par==0:
            print("Não tem nenhum valor par.")
            #Os valores pares forma x, y, z,...
            #Não tem nunhum valor par.
    case 76:       
        #Ter uma tupla única, com nomes de produtos e seu respectivos preços, na sequência.
        produtos=("Lápis", 1.75, "Borracha", 2.00, "Caderno", 15.90, "Estojo", 25.00, "Transferidor",  4.20, "Compasso", 9.99, "Mochila", 120.32, "Canetas", 22.30, "Livro", 34.90 )
        #Mostrar os dados de forma tabular.
        print("-"*40)
        print(f"{"LISTAGEM DE PREÇOS":^40}")#centraliza o texto em um espaço de 40 caracteres.
        print("-"*40)
        tamanho=0
        for maior in range(1, len(produtos),2):#frescura, so para ajustar o posição dos valores em relação ao R$
            if tamanho<len(str(produtos[maior])):
                tamanho=len(str(produtos[maior]))

        for cont in range(0,len(produtos),2):
                print(f"{produtos[cont]:.<30}R$ ",end="")#completa com "pontos" até completar 30 posições(caracteres).Alinha à esquerda
                print(f"{produtos[cont+1]:>{tamanho}.2f}")#Alinha à direita em X caracteres e formata para ponto flutuante com duas casas decimais
        #Lapis.........  R$1.75
        #Borracha......  R$2.00
        print("-"*40)

    case 77:
       #Uma tupla com várias palavras, mostrar para cada palavra quais são as sua vogais.
       palavras=("aprender", "programar", "linguagem", "python", "curso", "gratis", "estudar", "praticar", "trabalhar", "mercado", "programador", "futuro")
       #Na palavra APRENDER temos a e e
       for p in palavras:
            gambiarra='\nNa palavra'+ p.upper()+' temos'
            print(f'{gambiarra:.<30}:',end= " ")
            #print(f'\nNa palavra {p.upper()} temos:',end='')
            for letra in p:
                if letra.lower() in "aeiou":
                   print(letra,end=" ")

    case 78:
       #Ler 5 valores(int) e guardar em uma lista
            #Assim:
                #Digite um valor para a posição x:
        lista=[]
        for posicao in range(5):
           lista.append(int(input(f'Digite um valor para a posição {posicao}: ')))
        print(f"Você digitou os valores: {lista}")
        print(f"O maior valor digitado foi {max(lista)} na(s) posiçâo(óes) ",end="")
        for pos, vr in enumerate(lista):
            if vr >= max(lista):
                print(f"{pos}..",end="")
        print(f"\nO menor valor digitado foi {min(lista)} na(s) posiçâo(óes) ",end="")
        for pos, vr in enumerate(lista):
            if vr <= min(lista):
                print(f"{pos}..",end="")            
       #Mostrar qual maior e o menor e suas respectivas posições na lista
            #Caso apareça um valor repetido deverá ser informado todas as suas posições

    case 79:
       #Digitar vários valores e cadastrar em uma lista.
        lista=[]
        while True:
            n=int(input("Digite um valor: "))
            if n not in lista:
               lista.append(n)
               print("Valor adicionado com sucesso...")
            else:
               print("Valor duplicado! Não vou adicionar...")
            r=str(input("Quer continuar? [S/N]").upper())
            if r=="N":
                break
        print(sorted(lista))
            
       #Caso caso o valor ja exista ele não deve ser cadastrado outra vez
            #Valor duplicado! Não vou adicionar..
            #Quer continuar?
       #Mostrar todos eles (únicos) em ordem crescente.

    case 80:
        lista=[]
        #Digitar 5 valores e cadastrar em uma lista,
        #ja na posição correta da ordem crescente (sem usar sort())
        for c in range(0,5):
            n=int(input("Digite um valor: "))  
            if c== 0 or n > lista[-1]:
                lista.append(n)
                print("Adicionado ao final da lista...")          
            else:
                pos=0
                while pos < len(lista):
                    if n<=lista[pos]:
                        lista.insert(pos,n)
                        print(f"Adicionado na posição {pos} da lista...") 
                        break
                    pos+=1
        print(f"Os valores digitados, em ordem, foram {lista}")        
            #Digite um valor:
                #Adicionado ao final da lista... ou
                #Adicionada na posição X da lista...
        #Mostrar a lista ordenada no final
    
    case 81:        
        #Ler vários números e colocar em uma lista
        lista=[]
        while True:
            lista.append(int(input("Digite um valor: ")))
            opcao=""
            while opcao not in "SN" or opcao=="":
                opcao=str(input("Deseja continuar? [S/N]").upper())
            if opcao=="N":                    
                break
        lista.sort(reverse=True)
        print(f"A lista em ordem decrescente é {lista}")
        print(f"Voce digitou {len(lista)} elementos")        
        print(f'O valor 5', f'faz parte da lista!' if 5 in lista else f'não foi encontrado na lista!')
            #Quer continuar?
                #Mostrar quantos números forma digitados
                    #Voce digitou x elementos.
                #Mostrar a lista em ordem decrescnete
                    #Os valores em ordem decrescente são [x, y, z, ...]
                #Mostrar se o valor 5 foi digitado e está ou não na lista
                    #O valor 5 faz parte da lista!
                    #O valor 5 não foi encontrado na lista.

    case 82:        
        #Ler vários valaores e colocar em uma lista
        lista=[]
        pares=[]
        impares=[]
        while True:
            #Digite um valor:
            lista.append(int(input("Digite um valor: ")))
            #Quer continuar?
            opcao=""
            while opcao not in "SN" or opcao=="":
                opcao=str(input("Quer continuar? [S/N]").upper())
            if opcao=="N":
                break
        for item in lista:
            if item%2==0:
               pares.append(item)
            else:
                impares.append(item)                 
        print(f'A lista completa é {lista}')
        print(f'A lista de pares é {pares}')
        print(f'A lista de impares é {impares}')
        #Depois da lista criada, cria outras duas, a partir da primeira:
            #Uma contendo os valores pares e outra com valores impares.
        #Mostrar o conteudo das 3 listas.
            #A lista completa é [x, y, z, ...]
            #A lista de pares é [x, y, z, ...]
            #A lista de impares é [x, y, z, ...]

    case 83:        
        #Digitar uma expressão qualquer.
        expr=str(input("Digite a expressão:"))
        pilha=[]
        for simb in expr:
            if simb == "(":
                pilha.append("(")
            elif simb == ")":
                if len(pilha)>0:
                    pilha.pop()
                else:
                    pilha.append(")")
                    break
        if len(pilha)==0:
            print("Sua expressão está válida!")
        else:
            print("Sua expressão está errada")
            #((a+b)*c) correta
            #((a+b)*(a*c)-2 errada
        #Analisar se a expressão passada está com os parênteses abertos e fechados na ordem certa
        
    case 84:
        #Ler o nome e o peso de n pessoas, guarda em uma lista
        lista=[]
        while True:
            lista.append([input("Nome: "), float(input("Peso: "))])
            if len(lista) == 1:
                pesado=leve=lista[0][1]

            opcao=""
            while opcao not in 'SN' or opcao=="":
                opcao=str(input("Deseja continuar? [S/N]").upper())
            if opcao=="N":
                break
        print(f"Ao todo, você cadastrou {len(lista)} pessoas.")
        #Ao todo, você cadastrou x pessoas.
        for p in lista:
            if p[1]<=leve:
                leve=p[1]
            if p[1]>=pesado:
                pesado=p[1]

        print(f'O maior peso foi de {pesado} kg. Peso de ',end="")
        for p in lista:
            if p[1]>=pesado:
                print(f"[{p[0]}] ", end="")
        print(f'\nO menor peso foi de {leve} kg. Peso de ', end="")
        for p in lista:
            if p[1]<=leve:
                print(f"[{p[0]}] ", end="")          

        #O maior peso foi de X kg. Peso de fulano e ....
        #O menor peso foi de X kg. Peso de fulano e ....    

    case 85:
        numeros=[[],[]]
        for n in range(1,8):
            num=int(input(f"Digite o {n}º valor: "))
            if num%2==0:
                numeros[0].append(num)
            else:
                numeros[1].append(num)

        numeros[0].sort()
        numeros[1].sort()
        print(f"Os valores pares digitados forma: {numeros[0]}")
        print(f"Os valores impares digitados forma: {numeros[1]}")
        #Ler 7 valores, cadastra-los em uma única lista que mantenha separados os pares e os impares.[[pares],[impares]]
            #Digite o xº valor:
        #Mostrar os valores pares e impares em ordem crescente.

    case 86:        
        #Criar uma matriz 3x3 e preecher os valores lidos pelo teclado.
        #..., ..., ...
        #..., ..., ...
        #..., ..., ...
            #Digite um valor para a posição [0, 0]: até [2,2]. Guardar em uma lista única.
        #Mostrar assim:
        #[][][]
        #[][][]
        #[][][]
        matriz=[[0,0,0],[0,0,0],[0,0,0]]
        for l in range(0,3):
            for c in range(0,3):
                matriz[l][c]=int(input(f"Digite um valor para a posição [{l},{c}] "))
        for l in range(0,3):
            for c in range(0,3):
                print(f"[{matriz[l][c]:^5}]", end="")
            print()

    case 87:
        matriz=[[0,0,0],[0,0,0],[0,0,0]]
        for l in range(0,3):
            for c in range(0,3):
                matriz[l][c]=int(input(f"Digite um valor para a posição [{l},{c}] "))
        somapar=somacolunatres=0
        for l in range(0,3):
            for c in range(0,3):
                print(f"[{matriz[l][c]:^5}]", end="")
                if matriz[l][c]%2==0:
                    somapar+=matriz[l][c]
                if c==2:
                    somacolunatres+=matriz[l][c]
                
            print()
        #Aprimore o exercício anterior e mostre no final
        print(f"A sosma de todos os valores pares é {somapar}")
            #A soma de todos os valores pares
        print(f"A soma dos valores da 3ª coluna é {somacolunatres}")
            #A soma do valores da 3ª coluna
        print(f"O maior valor da 2ª linha é {max(matriz[1])}")
            #O maior valor da 2ª linha    

    case 88:
        print("-=-" * 12)        
        print("JOGA NA MEGA SENA".center(35))
        print("-=-" * 12)
        qtde=int(input("Quantos jogos voce que eu sorteie? "))
        print(f"SORTEANDO {qtde} JOGOS".center(35))
        #Quantos jogos você quer que sorteie?
        palpites=[]
        jogos=[]
        for j in range(1,qtde+1):
            palpites.clear()
            while len(palpites)<6:
                sorteio=random.randint(0,60)
                if sorteio not in palpites:
                    palpites.append(sorteio)
            palpites.sort()
            jogos.append(palpites[:])
        #print(f"Jogos {jogos}")
        for c, j in enumerate(jogos):
            print(f"Jogo {c+1}: {j}")
            time.sleep(1)
        #Cadastrar todos em uma única lista.
            #Sorteando X jogos
            #jogo 1: [a,b,c,d,e,f]
            #jogo 2: [a,b,c,d,e,f]
        #Os números sorteados não pode se repetir, no mesmo jogo

    case 89:
        pass
        #Ler o nome e duas notas de n alunos e guarda tudo em uma unica lista
        lista=[]
        #posicao=0
        while True:
            aluno=[0,[0,0],0]
            nome=str(input("Nome: "))
            nota1= float(input("Nota 1: "))
            nota2= float(input("Nota 2: "))
            lista.append([nome,[nota1,nota2],(nota1+nota2)/2])
            opcao=''
            while opcao not in 'SN' or opcao == "":
                opcao=str(input("Quer continuar? [S/N] ").upper())
            if opcao=="N":
                break
        print("-=-" * 15)
        print(f"{'Nº':<4} {'NOME':<10} {'MÉDIA':>8}")
        print("=" * 40)
        for i, a in enumerate(lista):
            print(f"{i:<4}{a[0]:<10}{a[2]:>8.1f}")
        print("=" * 40)
        while True:            
            while True:
                mostrar_notas=""
                try:
                    mostrar_notas=int(input("Mostrar notas de qual aluno? (999 interrompe): "))
                    if mostrar_notas==999:
                        break
                    print(f"Notas de {lista[mostrar_notas][0]} são {lista[mostrar_notas][1]}")

                except:
                    print("Digite o número de um aluno ou 999 para interromper!")
            if mostrar_notas==999:
                break

            #[[nome, [notas], média],[nome, [notas], média]]
        #Mostrar um boletim contendo a média de cada um e permitir ao usuário mostrar as notas de cada aluno individualmente.
            #Nome:
            #Nota 1:
            #Nota 2:
            #Quer continuar?

            #Mostrar assim:
            #Nº NOME    MÉDIA
            #0  Pedro   x.y
            #1  Maria   x.y
            #2  João    x.y
            #3  Edson   x.y

            #Mostrar notas de qual aluno? (999 interrompe):
                #Notas de xxxxx são [nota1, nota2]
                #Perguntar novamente...

    case 90:
        pass
        #Ler o nome é a média de um aluno, guardar tb a situação em um dicionário. No final mostre o conteúdo da estrutura na tela
        boletim={"nome":"aluno", "media":0, "situacao":""}
        boletim["nome"]=str(input("Nome: "))
        boletim["media"]=float(input(f'Média de {boletim['nome']} '))
        print("=" * 40)
        if boletim["media"]>=7:
            boletim["situacao"]="aprovado"
        elif boletim["media"]>=5:
            boletim["situacao"]="recuperação"
        else:
            boletim["situacao"]="reprovado"
        for chave, valor in boletim.items():
            print(f"- {chave.capitalize()} é igual a {valor}")#capitalize para a primeira letra para miúsculo

            #Nome:
            #Media de fulano:
                #Nome é igual a fulano
                #Media é igual a xxx
                #Situação é igual a Aprovado/Reprovado

    case 91:
        pass
        #4 jogadores jogam um dado e tenham resultados aleatório. Guardar os resultados em um dicionário. No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado.
        jogos={"jogador 1":random.randint(1,6),
               "jogador 2":random.randint(1,6),
               "jogador 3":random.randint(1,6),
               "jogador 4":random.randint(1,6)}
        print("=" * 40)
        print("Valores sorteados".center(40))
        print("=" * 40)
        for chave, valor in jogos.items():
            print(f"O {chave} tirou {valor} no dado")
            time.sleep(1)

        ordem={}#é um dicionário mas a linha abaixo faz uma "list". Mas o "dict" refaz para dicionário
        ordem = dict(sorted(jogos.items(), key=itemgetter(1), reverse=True)) #ordena os jogos pelo valor(1)
        ordem2=sorted(jogos, key=jogos.get, reverse=True) #faz o mesmo que a linha acima.
        print("=" * 40)
        print("Ranking dos jogadores".center(40))
        print("=" * 40)
        c=1
        for chave, valor in ordem.items():
            print(f"{c}º lugar: {chave} com {valor}".center(40))
            c+=1
            time.sleep(1)
            #Valores sorteados:
                #O jogador1 tirou x
                #O jogador2 tirou y...
            #Ranking dos jogadores:
                #1º lugar: jogador... com xxx
                #2º lugar....

    case 92:
        pass
        #Ler o nome, ano de nascimento, a CTPS e cadastra-os(com idade) em um dicionário se por acaso a CTPS for diferente de ZERO, o dicionário receberá tb o ano de contratação e o salário. Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.
        cadastro={}
        cadastro["nome"]=str(input("Nome: "))
        nasc=int(input("Ano de Nascimento: "))
        cadastro["idade"]=datetime.date.today().year-nasc
        cadastro["ctps"]=int(input("Carteira de Trabalho (0=não tem): "))
        if cadastro["ctps"]!="0":
            cadastro["contração"]=int(input("Ano de contratação: "))
            cadastro["salário"]=float(input("Salário: "))
            cadastro["aposentadoria"]=cadastro["idade"]+((cadastro["contração"]+35) - datetime.date.today().year)
        print("=" * 40)
        for chave, valor in cadastro.items():
            print(f"- {chave} tem o valor {valor}")
        print("=" * 40)
            #Nome:
            #Ano de nascimento:
            #CTPS (0 não tem):
            #Ano de contratação:
            #Salário: R$...
                #Mostrar o dicionário
                #nome tem valor....
                #idade tem valor....
                #ctps tem valor...
                #contratação tem valor...
                #salário tem o valor ....
                #aposentadoria em o valor ...
            #Se CTPS for zero:
                #nome tem valor....
                #idade tem valor....
                #ctps tem valor...

    case 93:
        #Gerenciar o aproveitamento de um jogador de futebol. Ler o nome do jogador e quantas partidas ele jogou. Depois ler a quantidade de gols feitos em cada partida. No final, tudo guardade em um dicionário, incluindo o total de gols feitos durante o campeonado.
        futebol={}
        gols=[]
        futebol["jogador"]=str(input("Nome do Jogador: "))
        futebol["partidas"]=int(input(f"Quantas partidas {futebol['jogador']} jogou? "))
        for p in range (futebol["partidas"]):
            gols.append(int(input(f"    Quantos gols na partida {p+1}? ")))
        futebol["gols"]=gols.copy()
        futebol["total"]=sum(gols)
        print("=" * 75)
        print(futebol)
        print("=" * 75)
        for chave, valor in futebol.items():
            print(f"O campo {chave} tem o valor {valor}")
        print("=" * 75)
        print(f"O jogador {futebol['jogador']} jogou {len(futebol['gols'])} partidas.")
        contador=1
        for chave, valor in enumerate(gols):
            print(f"==> Na partida {chave+1}, fez {valor} gol(s)".center(40))
        print(f"Foi um total de {futebol['total']} gol(s)")
        
            #Nome do jogador:...
            #Quantas partidas .... jogou?...
                #Quantos gols na partida 1?
                #Quantos gols na partida 2?...
        #Mostrar o dicionário:
            #{"nome":"fulano", "gols":[x, y, z, ...], "total":...}
            #O campo nome tem o valor ...
            #O campo gols tem o valor [x, y, z, ...]
            #O campo total tem o valor ...
                #O jogador .... jogou ... partidas.
                    # - Na partida ..., fez ... gols.
                    # - Na partida ..., fez ... gols.
                    # - Na partida ..., fez ... gols.
                #Foi um total de ... gols                  

    case 94:
        #Ler o nome, sexo e idade de n pessoas, guardar os dados de cada um em um  dicionário e todos os dicionário em uma lista.
        lista=[]
        dicionario={}
        somaidade=0
        while True:
            dicionario.clear()
            dicionario["nome"]=str(input("Nome: "))
            while True:
                opcao=str(input("Sexo: [M/F] ").upper())
                if opcao in "MF" and opcao!="":
                    break
                print("ERRO! Responda apenas M ou F")
            dicionario["sexo"]=opcao
            while True:
                try:
                    idade=int(input("Idade: "))
                    somaidade+=idade
                    break                    
                except:
                    print("ERRO! Digite apenas numeros inteiros!")                    
            dicionario["idade"]=idade            
            print(dicionario)
            while True:
                opcao=str(input("Quer continuar? [S/N] ").upper())
                if opcao in "SN" and opcao!="":
                    break
                print("ERRO! Responda apenas S ou N")
            lista.append(dicionario.copy())
            if opcao=="N":
                break
        print(lista)
        print("=" * 75)
        print(f"A) Ao todo temos {len(lista)} pessoas cadastradas")
        print(f"B) A média de idade é de {somaidade/len(lista):.2f} anos.")

        print(f"C) As mulheres cadastradas foram ", end="")
        for sx in lista:
            if sx["sexo"]=="F":
                print(f"{sx["nome"]}", end=" ")

        print(f"\nD) Lista das pessoas que estão acima da média de {somaidade/len(lista):.2f} anos:")
        for am in lista:
            if am["idade"]>somaidade/len(lista):
                print(f"Nome = {am["nome"]}; Sexo = {am["sexo"]}; Idade = {am["idade"]}".center(40))
        
        #Nome:
        #Sexo [M/F]:
        #Idade:
        #Quer continuar?

        # No final, mostre:
            #Quantas pessoas foram cadastradas
                #O grupo tem ... pessoas
            #A média de idade do grupo
                #A média de idade é de ... anos
            #Uma lista com todas as mulhres
                #As mulheres cadastradas foram: ...., ....
            #Uma lista com todas as pessoas com idade acim da média.
                #nome = ...., sexo = ..., idade = ...

    case 95:
        pass
        #Aprimore o desafio 93, para que ele funcione com vários jogadores, incluindo um sistema de visualização de detalhes do aproveitamento de cada 
        time=[]
        jogador={}
        partidas=[]
        while True:
            jogador.clear()
            jogador['nome']= str(input("Nome do jogador: "))
            while True:
                try:
                    tot = int(input(f"Quantas partidas {jogador['nome']} jogou? "))
                    break
                except:
                    print("*** ERRO *** Digite apenas números inteiros")
            partidas.clear()
            for c in range(0,tot):
                while True:
                    try:
                        partidas.append(int(input(f"   Quantos gols na partida {c+1}? ")))
                        break
                    except:
                        print("*** ERRO *** Digite apenas números inteiros")
            jogador['gols'] = partidas[:]
            jogador['total'] = sum(partidas)
            time.append(jogador.copy())
            while True:
                resp = str(input("Quer continuar? [S/N] ")).upper()
                if resp in 'SN' and resp!="":
                    break
                print("ERRO! Responda apenas S ou N")
            if resp == "N":
                break
        print('-=' * 30)
        print('cod ' , end='')
        for i in jogador.keys():
            print(f'{i:<15}', end="")
        print()
        print('-' * 40)
        for k, v in enumerate(time):
            print(f'{k+1:>3} ', end="")
            for d in v.values():
                print(f'{str(d):<15}', end="")
            print()
        print('-' * 40)
        while True:
            while True:
                try:
                    busca = int(input('Mostra dados de qual jogador? (999=sair) '))
                    break
                except:
                    print("*** ERRO *** Digite apenas números inteiros")
            busca-=1 #artifício para não aparecer jogador zero.
            if busca == 998:
                break
            if busca >= len(time):
                print(f'ERRO! Não existe jogado com o código {busca}!')
            else:
                print(f'  -- LEVANTAMENTO DO JOGADOR {time[busca]['nome']}:')
                for i, g in enumerate(time[busca]['gols']):
                    print(f'    No jogo {i+1} fez {g} gol(s)')
                print('-' * 40)
        print('<< VOLTE SEMPRE >>')
        # jogador.
            #Nome do jogador:
            #Quantas partidas...jogou?
            #Quantos gols na partida ...?
            #Quer continuar?

            #Mostrar:
                #cod nome           gols            total
                # 0. fulano         [ , , ]         .....

                #Mostrar dados de qual jogador? (999 para)
                    #Levantamento do jogador ...:
                    #No jogo ...fez ...gols.
                    #No jogo ...fez ...gols.
                    #Se for escolhi um jogador que não existe (codigo):
                        #ERRO! Não existe jogador com o código ...! Tente novamente.
                    
                #Mostrar dados de qual jogador?....

    case 96:        
        #Criar uma funçao, chamada area() que receba as dimensões de um terreno retangular e mostre a área do terreno.
        def area(largura,comprimento):
            a=largura*comprimento
            print(f'A área de um terreno de {largura}x{comprimento} é de {a}m²')
            
        print('Controle de área')
        l=float(input('Largura (m): '))
        c=float(input('Comprimento (m): '))
        area(l,c)
            #Controle de área de terrenos
                #Largura (m): xxx
                #Comprimento (m): xxx
                    #A área de um terreno  de ... X ... é de ......

    case 97:        
        #Faça um função chamada escreva(), que receba um texto qualquer com parâmetro e mostre uma msg com tamanho adaptável, ou seja, o tamanho das linhas acompanha o tamanho do texto.
        #Ex.: escreva("Ola, Mundo!")
            #saida:   ~~~~~~~~~~~~~~
            #           Ola, Mundo!
            #         ~~~~~~~~~~~~~~  
        def escreva(texto):
            tam=len(texto)+4
            print('~' * tam)
            print(f'{texto}'.center(tam))      
            print('~' * tam)

        escreva("Edson Gomes dos Santos")
        escreva("Olá! Mundo!")

    case 98:
        pass
        #Faça uma função chamada contador(), que receba 3 parâmetros (inicio, fim, passo) e realize a contagem
        def contador(inicio, fim, passo):
            print('=' * 30)
            print(f'Contagem de {inicio} até {fim} de {abs(passo)} em {abs(passo)}')
            if passo==0:
                passo=1
            if passo<0:
                passo*=-1
            if inicio>fim and passo<0:
                 fim-=2
            if inicio>fim and passo>0:
                passo=-passo
                fim-=2
            for n in range(inicio, fim+1, passo):
                print(f'{n}',end=' ', flush=True)#flush atualiza a tela(por causa do sleep)
                time.sleep(.5)
            print('FIM!')

        contador(1,10,1)
        contador(10,0,2)
        print('=' * 30)
        print('Agora é sua vez de personalizar a contagem!')
        i=int(input('Início: '))
        f=int(input('Fim: '))
        p=int(input('Passo: '))
        contador(i,f,p)
        #Realizar 3 contagens:
            #De 1 até 10, de 1 em 1
            #De 10 até 0, de 2 em 2
            #Personalizda, o usuário vai passar os parâmetros.
                #Contagem de 1 até 10 de 1 em 1:
                #1 2 3 4 ...FIM
                #Contatem de 10 até 0 de 2 em 2
                #10 8 6 4 ...FIM
                #Agora é sua vez de personalizar a contagem!
                    #Nesse caso deve aceitar passo negativo tb e contagem regressiva
                    #Início: ...
                    #Fim: ...
                    #Passo: ...
                        #Contagem de ... até ... de ... em ...
                        #x y z ... FIM

    case 99:        
        #Faça um funão maior(*p) e analizar todos os valores passados e dizer qual é o maior
        def maior(*p):
            cont=maior=0
            print('=' * 30)
            print('Analisando os valores passados...')
            for num in p:
                print(f'{num}', end=' ', flush=True)
                time.sleep(.5)
                if cont==0:
                    maior=num
                else:
                    if num>maior:
                        maior=num
                cont+=1
            print(f'Foram informados {cont} valores ao todo.')
            print(f'O maior valor informado foi o {maior if p else 0}')

        maior(2,9,4,5,7,1)
        maior(4,7,0)
        maior(-1,-2)
        maior(6)
        maior()
            #Analisando os valores passados...
            # x y z... Foram informados ... valores ao todo
            # O maior valor informado foi ...

    case 100:
        pass
        #Faça um prog. que tenha uma lista chamada números e duas funções chamadas sorteio() e somaPar(). A primeira vai sortear 5 números aleatórios e colocar na lista e a segunda vai mostrar a soma dos valores pares sorteados.
            #Sorteando ... valores da lista: x y z ... PRONTO!
            #Somando os valores pares de ...., temos ...
        lista={}
        numeros=[]
        def sorteio():
            print(f'Sorteando 5 numeros da lista: ', end='')
            for v in range(0,5):
                valor=random.randint(0,10)
                numeros.append(valor)
                print(f'{valor}', end=' ', flush=True)
                time.sleep(1)
            print('PRONTO!')

        def somaPar(n):
            soma=0
            for s in n:
                if s%2==0:
                    soma+=s
            print(f'Somando os valores pares de {n}, temos {soma}')

        sorteio()
        somaPar(numeros)

    case 101:
        pass
        #Cria uma função chamada voto() que vai receber um parâmetro o ano de nascimento de uma pessoa e retornar um valor literal, dizendo se a pessoa tem voto opcional, negado ou obrigatório.
        def voto(nascimento):
            agora=datetime.date.today().year
            idade=agora-nascimento
            if idade<16:
                return f"Com {idade} anos voce não vota!"
            elif idade>=65 or idade<18:
                return f"Com {idade} anos o voto é opcional"
            else:
                return f"Com {idade} anos o voto é obrigatorio!"
            #Em que ano vocé nasceu? ...
        nasc=voto(int(input('Em que ano você nasceu? ')))
        print(nasc)
                #Com ... anos: "Voto....."
                #obs. Mais de 65 anos o voto é opcional

    case 102:        
        #Criar uma função fatorial() que receba dois parâmetros: O 1º que indique o número a calcular e o 2º chamado 'show', que será um valor lógico(opcional) indicando se será mostrado ou não na tela o processo de cálculo do fatorial
        def fatorial(n=1, show=False):
            """
            -> Calcula o fatorial de um número.
            :param n: O número a ser calculado
            :param show: (opcional) Mostrar ou não a conta.
            :return: O valor do fatoria de um número n.
            """
            f=1
            for c in range(n, 0, -1):
                if show:
                    print(c,end='')
                    if c>1:
                        print(' x ', end='')
                    else:
                        print(' = ', end='')
                f*=c                
            return f
        print(fatorial(5, show=True))
        help(fatorial)

    case 103:
        #Fazer uma função ficha(), que receba dois parâmetros opcionais, 'nome' de um jogador e quantos 'gols' ele marcou.
        def ficha(n='<desconhecido>',g=0):
            print(f'O jogador {n} fez {g} gol(s) no campeonato.')
        
        nome=str(input('Nome do Jogador: '))
        gols=str(input('Número de gols: '))
        if gols.isnumeric():
            gols=int(gols)
        else:
            gols=0
        if nome.strip()=='':#se o nome for vazio passa apenas o parâmetro 'g'
            ficha(g=gols)
        else:
            ficha(nome, gols)
        #Mostrar a ficha do jogador, mesmo que algum dado não tenha sido informado corretamente.
            #Nome do Jogador: .... se não informar mostrar <desconhecido>
            #Número de gols: ... se não informar mostrar zero gol(s)
                #O jogador ... fez ... gol(s) no campeonado.

    case 104:        
        #Criar uma função leiaint(), que vai funcionar de forma semelhante à função 'input' do python, so que fazendo a validação para aceitar apenas um vr numérico
        #Ex.:
        def leiaint(texto):
            while True:
                try:
                    n=int(input(texto))
                    return n
                except:
                    print('\033[0;31mERRO! Digite um número inteiro válido.\033[m]')
            
        n=leiaint('Digite um número: ')
        print(f'Voce acabou de digitar o número {n}')
                #Digite um número:...
                #Vocé acabou de digitar o número ...
                    #ou ERRO! Digite um número inteiro válido.
        
    case 105:        
        #Criar uma função notas() que pode receber várias notas de alunos e vai retornar um dicionário com as seguintes informações:
            # - Quantidade de notas
            # - A maior nota
            # - A menor nota
            # - A média da turma
            # - A situação(opcional): boa, razoável, ruim
        def notas(*n, sit=False):
            """
            -> Função para analisar notas e situações de vários alunos.
            :param n: uma ou mais notas dos alunos (aceita várias)
            :param sit: valor opcional, indicando se deve ou não adicionar a situação
            :return: dicionário com várias informaçãoes sobre a situação da turma.
            """
            boletim={}
            boletim['total']=len(n)
            boletim['maior']=max(n)
            boletim['menor']=min(n)
            boletim['media']=sum(n)/len(n)
            if sit:
                boletim['situação']='Razoável'
                if sum(n)/len(n)>=7:
                    boletim['situação']='Boa'
                if sum(n)/len(n)<5:
                    boletim['situação']='Ruim'                    
            return boletim
        resp= notas(8.5, 9, 10, 5.5, 2.5, sit=True)
        print(resp)
        help(notas)
            #{'total': 4, 'maior': 10, 'menor': 5.5 'média': 7.875, 'situação': 'Boa'}

    case 106:
        
        #Faça um mini-sistema que utilize o interactive help do python. O usuário vai digitar o comando e o manual vai aparecer. Quando o usuário digitar FIM o programa acaba.
        #OBS. Usar cores
                #Verde cocô
            #~~~~~~~~~~~~~~~~~~~~~~~~~~~~
            #  SISTEMA DE AJUDA PyHELP              colacar em um loop
            #~~~~~~~~~~~~~~~~~~~~~~~~~~~~
            #Função ou Biblioteca>...(ex.: 'len')   tb no loop
        c=('\033[m',           #0 - sem cores
        '\033[0;30;41m',     #1 - vermelho
        '\033[0;30;42m',     #2 - verde
        '\033[0;30;43m',     #3 - amarelo
        '\033[0;30;44m',     #4 - azul
        '\033[0;30;45m',     #5 - roxo
        '\033[7;30m',        #6 - branco
            )


        def ajuda(com):
            titulo(f'Acessando o manual do comando \'{com}\'', 4)
            print(c[6], end='')
            help(com)
            print(c[0])
            #time.sleep(2)


        def titulo(msg, cor=0):
            tam=len(msg)+4
            print(c[cor], end='')
            print('~'*tam)
            print(f'  {msg}')
            print('~'*tam)
            print(c[0])
            #sleep(1)

        comando=''
        while True:
            titulo('SISTEMA DE AJUDA PyHELP', 2)
            comando=str(input('Função ou Biblioteca (FIM=SAIR) => '))
            if comando.upper()=='FIM':
                break
            else:
                ajuda(comando)
        titulo('Até logo!',1)

                #Azul, quase Cruzeiro
            #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
            #  Acessando o manual do comando 'len'
            #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

            #se FIM
                #vermelho, quase rosa.
            #~~~~~~~~~~~~
            #  ATÉ LOGO!
            #~~~~~~~~~~~~

    case 107:        
        #crie um módulo chamado moeda.py que tenha as funções incorporadas:
            #aumentar()
            #diminuir()
            #dobro()
            #metade()
        #Fazer um progrma que importe esse módulo e use algumas dessas funções.
        pass

    case 108:
        #Adapte o desafio 107, criando um função adicional chamada moeda() que consiga mostrar os valores com um valor monetário formatado.
        pass
        

    case 109:        
        #Modifique as funções que foram criadas no desafio 107 para que elas aceitem um parâmetro a mais, informando se o valor retornado por elas vai ser ou não formatado pela função moeda(), desenvolvido no desafio 108
        pass

    case 110:            
            #Adicione ao móduto moeda.py criado nos desafios anteriores, um função chamada resumo(), que mostre na tela algumas informações geradas pelas funções que ja temos no módulo criado até aqui
            pass

            #Resultado:
                #~~~~~~~~~~~~~~~~~~
                # Resumo do valor
                #~~~~~~~~~~~~~~~~~~
                #Preço analisado:   R$...
                #Dobro do preço:    R$...
                #Metado do preço:   R$...
                #80% de aumento:    R$...
                #35% de redução:    R$...
                #-------------------------

    case 111:
            pass
            #Crie um pacote chamado utilidadesCev que tenha dois módulos internos chamados moeda e dado.
            #Transfira todas a funções utilizadas nos desafios 107 a 110 para o primeiro pacote e mantenha tudo funcionando.
            
            #Resultado:
                #~~~~~~~~~~~~~~~~~~
                # Resumo do valor
                #~~~~~~~~~~~~~~~~~~
                #Preço analisado:   R$...
                #Dobro do preço:    R$...
                #Metado do preço:   R$...
                #80% de aumento:    R$...
                #35% de redução:    R$...
                #-------------------------

    case 112:
            pass
            #Dentro do pacote utilidadescev que foi criado no desafio 111, temos um módulo chamado dado. Crie uma função chamada leiaDinheiro() que seja capaz de funcionar como a função input(), mas com uma validação de dados para aceitar apenas valores que sejam monetários.
                #Obs.: aceitar valores com decimal de ponto ou vírgula.

    case 113:
            pass
            #Reescreva a função leiaint(), desafio 104, incluindo agora a possiblidade da digitação de um número de tipo inválido. Aproveite e crie também uma função leiaFloat() com a mesma funcionalidade
                #Digite um inteiro: ...
                    #se erro:
                        #'ERRO: por favor, digite um número inteiro válido.
                    #se interrompido:
                        #'Usuário preferiu não digitar esse número.
                        #'O valor inteiro digitado foi 0(zero)
                #Digite um Real:....
                    #se erro:
                        #'ERRO: por favor, digite um número real válido.
                    #se interrompido:
                        #'Usuário preferiu não digitar esse número
                        #'O valor inteiro digitado foi... e o real foi 0(zero)
                #o valor inteiro digitado foi ....e o real foi ...
            def leiaint(num):
                while True:
                    try:
                        n=int(input(num))
                        return n
                    except KeyboardInterrupt:
                        print('O usuário preferiu não informar os dados')
                        return 0
                    except: 
                        print('\033[0;31mERRO! Digite um número inteiro válido.\033[m]')

            def leiaFloat(num):
                while True:
                    try:
                        n=float(input(num))
                        return n
                    except KeyboardInterrupt:
                        print('O usuário preferiu não informar os dados')
                        return 0
                    except:
                        print('\033[0;31mERRO! Digite um número real válido.\033[m]')
      
            
            n=leiaint('Digite um número: ')
            r=leiaFloat('Digite um número real: ')
            print(f'O valor inteiro digitado foi {n} e o real foi {r}')
                        
    case 114:
            pass
            #crie um código em python que teste se o site 'pudim' está acessível pelo computador usado.
                #play:
                    #Consegui acessar o site pudim com sucesso
                    #O site pudim não está acessível no momento
            #import urllib
            #import urllib.request
            try:
                site=urllib.request.urlopen('http://www.globo.com.br')
                print('Site está acessível')
            except:
                print('Site não está acessível')            


    case 115:
            pass
            #Crie um sistema modularizado que permita cadastrar pessoas pelo seu nome e idade em um arquivo de texto simples.
            #O sistema so vai ter 2 opções: Cadastrar um nova pessoa e Listar todas as pessoas cadastradas.
                #---------------------------
                # Menu principal
                #---------------------------
                # 1 - Ver pessas cadastradas
                # 2 - Cadastrar nova pessoa
                # 3 - Sair do sistema
                #---------------------------
                #Sua opção:

                #se 1:
                #--------------------------------------
                # Pessoas cadastradas
                #--------------------------------------
                #...........            ...anos
                #...........            ...anos

                #volta a mostrar o menu principal

                #se 2:
                #--------------------------------------
                # Novo cadastro
                #--------------------------------------
                # Nome:....
                # Idade:...     tratar erros de digitação.
                #Novo registro de .... adicionado.

                #volta a mostrar o menu principal

                #se opção inválida
                #ERRO! Digite uma oção válida!

                #volta a mostrar o menu principal

                #se 3:
                #--------------------------------------
                # Saindo do sistema...Até logo!
                #--------------------------------------


    case 116:
            pass

    case 117:
            pass



        