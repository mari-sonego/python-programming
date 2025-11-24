from Arquivo import*

def mviagem(dic,voo,piloto):

    existeArqVi(dic)


    menu=0
    
    while menu != 6:
        print("\nﾉ༼༎ຶ⁠ Menu - Viagens ⁠༎ຶ⁠༽ﾉ\n")
        print("1 - Listar Todas As Viagens")
        print("2 - Listar Uma Viagem")
        print("3 - Adicionar Uma Viagem")
        print("4 - Alterar Uma Viagem")
        print("5 - Excluir Uma Viagem")
        print("6 - Voltar\n")
        a=int(input("Qual Opção Deseja Executar?:"))
        if a == 1:
            listarvi(dic)
        elif a == 2:
            tupla=input("Digite o nome do Voo:"),input("Digite o nome do Piloto:"),input("Digite a data da Viagem:"),input("Digite a hora da Viagem:")
            listarViagem(dic,tupla)
        elif a == 3:
            incluirViagem(dic,voo,piloto)
        elif a == 4:
            t=input("Digite o nome do Voo:"),input("Digite o nome do Piloto:"),input("Digite a data da Viagem:"),input("Digite a hora da Viagem:")
            alterarViagem(dic,t)
        elif a == 5:
            excluirvi(dic)
        elif a == 6:
            return
        else:
            print("ﾉ༼༎ຶ⁠ Opção Não Aceita! ༎ຶ⁠༽ﾉ")
            enter()


def percorre(BD, igual):

    return (igual in BD)

def enter():

    input('\n ﾉ༼༎ຶ⁠ Tecle <Enter> para continuar ༎ຶ⁠༽ﾉ \n')


def alterarParte(viagens, infVoo_m, ind, mud, qntd):

    lista = list(infVoo_m)

    lista[ind]= mud

    tem = percorre(viagens, tuple(lista))

    if (tem):

        print('\n » Piloto e viagem já existente!')
        enter()

    else:

        del viagens[infVoo_m]

        lista = tuple(lista)

        viagens[lista] = qntd

        print('\n ✔ Alteração feita com sucesso!')
        enter()

        return lista


def incluirViagem(viagens,voos,pilotos):

    print("\nﾉ༼༎ຶ⁠ Incluindo Piloto ⁠༎ຶ⁠༽ﾉ\n")

    numVoo = int(input ('\n ♦ Digite o Número de Voo: '))
    ex=percorre(voos, numVoo)
    while ex == False:

        numVoo = int(input ('\n ♦ Digite o Número de Voo novamente: '))
        ex=percorre(voos, numVoo)

    piloto = int(input('\n ♦ Digite o registro do piloto: '))
    ex2=percorre(pilotos,piloto)

    while ex2 == False:
        piloto = int(input('\n ♦ Digite o registro do piloto novamente: '))
        ex2=percorre(pilotos,piloto)

    data = input('\n ♦ Digite a data da viagem (dd.mm.aaaa): ')
    hora = input('\n ♦ Digite a hora da viagem: ')

    infVoo = (numVoo, piloto, data, hora)

    flag = percorre(viagens, infVoo)

    if (flag):

        print('\n ツ Viagem já cadastrada anteriormente. \n')
        enter()

    else:

        qntdPassageiros = int( input ('\n ♦ Digite a quantidade de passageiros que o avião terá: ') )

        viagens[infVoo] = qntdPassageiros

        print('\n ✔ Viagem cadastrada com sucesso! \n')
        enter()

    return


def alterarViagem(viagens, infVoo_m):  # infVoo_m é uma TUPLA

    print("\nﾉ༼༎ຶ⁠ Alterando Viagem ⁠༎ຶ⁠༽ﾉ\n")

    flag = percorre(viagens, infVoo_m)

    if (flag):

        opcao = 0

        while (opcao != 6):

            print('\n ✸ Menu de Alterações ✸ \n')
            print('1 ➸  Alterar o Número de Voo')
            print('2 ➸  Alterar o registro do piloto')
            print('3 ➸  Alterar a data da viagem')
            print('4 ➸  Alterar o hora da viagem')
            print('5 ➸  Alterar a quantidade de passageiros')
            print('6 ➸  Finalizar alteramento')

            opcao = int(input ('\n ♦ Digite a opção desejada: '))

            while (opcao < 1 or opcao > 6):
                opcao = int(input ('\n ♦ Número digitado fora do menu. Digite a opção desejada novamente: '))

            qntd= viagens[infVoo_m]

            if (opcao == 1):

                num = input ('\n ♦ Digite o novo Número de Voo: ')

                paraNova= alterarParte(viagens, infVoo_m, 0, num, qntd)

                infVoo_m= paraNova

            elif (opcao == 2):

                nome = int ( input('\n ♦ Digite o novo registro do piloto: ') )

                paraNova= alterarParte(viagens, infVoo_m, 1, nome, qntd)

                infVoo_m= paraNova

            elif (opcao == 3):

                data = input('\n ♦ Digite a nova data da viagem: ')

                paraNova= alterarParte(viagens, infVoo_m, 2, data, qntd)

                infVoo_m= paraNova

            elif (opcao == 4):

                hora= input ('\n ♦ Digite a nova hora da viagem: ')

                paraNova= alterarParte(viagens, infVoo_m, 3, hora, qntd)

                infVoo_m= paraNova

            elif (opcao == 5):

                qntdNova= int ( input ('\n ♦ Digite a nova quantidade de passageiros: ') )

                viagens[infVoo_m]= qntdNova

                print('\n ✔ Alteração feita com sucesso!')
                enter()

    else:
        print('\n ツ Viagem não cadastrada. \n')
        enter()   

def listarViagem(viagens, infVoo_l): # infVoo_l é uma TUPLA

    print("\nﾉ༼༎ຶ⁠ Listando Viagem ⁠༎ຶ⁠༽ﾉ\n")
        
    flag= percorre(viagens, infVoo_l)

    if (flag):

        numVoo, piloto, data, hora = infVoo_l
        qntdPas= viagens[infVoo_l]

        print (f'\n » Número de Voo: {numVoo}')
        print (f'» Registro do piloto: {piloto}')
        print (f'» Data da viagem: {data}')
        print (f'» Hora da viagem: {hora}')
        print (f'» Quantidade de passageiro: {qntdPas}')  

    else:
        print('\n ツ Viagem não cadastrada. \n')
        enter() 


def listarvi(dic):
    print("\nﾉ༼༎ຶ⁠ Listando todos as Viagens ⁠༎ຶ⁠༽ﾉ\n")
    for numero in dic.keys():
        a=numero
        print("» Número do Voo:",a[0])
        print("» Registro do Piloto",a[1])
        print("» Data da Viagem:",a[2])
        print("» Hora da Viagem:",a[3])
        c=dic.get(numero)
        print("» Quantidade de Passageiros:",c)
        print("\n")
    enter()

def excluirvi(dic):
    print("\nﾉ༼༎ຶ⁠ Excluindo um Viagem ⁠༎ຶ⁠༽ﾉ\n")
    numv=input("Digite o Número do Voo:"),int(input("Digite o registro do Piloto:")),input("Digite a Data do Voo:"),input("Digite a hora:")
    controle=False
    for numero in dic.keys():
        if numero == numv:
            controle=True
            a=numero
    if controle == False:
        print("\nﾉ༼༎ຶ⁠ Elemento não Encontrado ⁠༎ຶ⁠༽ﾉ\n")
    else:
        del dic[a]
        print ('\n ✔ Exclusão feita com sucesso!')
        enter()
    