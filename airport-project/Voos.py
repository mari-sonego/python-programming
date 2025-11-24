from Arquivo import*

def mvoos(dic):

    existeArqVoo(dic)

    menu=0
    while menu != 6:
        print("\nﾉ༼༎ຶ⁠ Menu - Voos ⁠༎ຶ⁠༽ﾉ\n")
        print("1 - Listar Todos Os Voos")
        print("2 - Listar Um Voo")
        print("3 - Adicionar Um Voo")
        print("4 - Alterar Um Voo")
        print("5 - Excluir Um Voo")
        print("6 - Voltar\n")
        a=int(input("Qual Opção Deseja Executar?:"))
        if a == 1:
            listarvo(dic)
        elif a == 2:
            voo=int(input("Digite o número do Voo:"))
            listarVoo(dic,voo)
        elif a == 3:
            incluirVoo(dic)
        elif a == 4:
            v=int(input("Digite o número do Voo:"))
            alterarVoo(dic,v)
        elif a == 5:
            excluirv(dic)
        elif a == 6:
            return
        else:
            print("ﾉ༼༎ຶ⁠ Opção Não Aceita! ༎ຶ⁠༽ﾉ")
            enter()

def percorre(BD, igual):

    return (igual in BD)

def enter():

    input ('\n ﾉ༼༎ຶ⁠ Tecle <Enter> para continuar ༎ຶ⁠༽ﾉ')

def incluirVoo(voos):

    print("\nﾉ༼༎ຶ⁠ Incluindo Voo ⁠༎ຶ⁠༽ﾉ\n")

    num= int ( input ('\n ♦ Digite o Número do Voo: ') )

    flag= percorre(voos, num)

    if (flag):
        print('\n ツ Voo já cadastrado anteriormente.')
        enter()

    else:

        cidadeOrigem= input ('\n ♦ Digite a sua cidade de origem: ')
        cidadeDestino= input ('\n ♦ Digite a sua cidade de destino: ')
        tempo= input ('\n ♦ Digite o tempo médio gasto na viagem:  ')
        aeronave= input ('\n ♦ Digite qual aeronave foi utilizada durante o voo: ')
        cidadesE= []
        cid= input ('\n ♦ Digite um nome da cidade de escalas ("0" para terminar): ')
        while (cid != '0'):
            cidadesE.append(cid)
            cid= input ('\n ♦ Digite um nome da cidade de escalas ("0" para terminar): ')
        
        inf= [cidadeOrigem, cidadeDestino, tempo, aeronave, cidadesE]

        voos[num]= inf 

        print('\n ✔ Voo cadastrado com sucesso! \n')
        enter()

    return 

def alterarVoo(voos, num_m):

    print("\nﾉ༼༎ຶ⁠ Alterando Voo ⁠༎ຶ⁠༽ﾉ\n")

    flag= percorre(voos, num_m)

    if (flag):

        opcao= 0

        while (opcao != 7):

            print ('\n ✸ Menu de Alterações ✸ \n')
            print ('1 ➸  Alterar o Número de Voo')
            print ('2 ➸  Alterar a cidade de origem')
            print ('3 ➸  Alterar a cidade de destino')
            print ('4 ➸  Alterar o tempo médio')
            print ('5 ➸  Alterar a aeronave')
            print ('6 ➸  Alterar as cidades das escalas')
            print ('7 ➸  Finalizar alteramento')

            opcao= int ( input ('\n ♦ Digite a opção desejada: ') )

            while (opcao < 1 or opcao > 7):
                opcao= int ( input ('\n ♦ Número digitado fora do menu. Digite a opção desejada novamente: ') )

            lista= voos[num_m]

            if (opcao == 1):

                # número de voo

                num= int ( input ('\n ♦ Digite o novo Número de Voo: ') )

                tem= percorre(voos, num)

                if (tem):
                    print ('\n » Número de Voo já existente!')
                    enter()

                else:

                    del voos[num_m] 

                    voos[num]= lista

                    num_m= num

                    print ('\n ✔ Alteração feita com sucesso!')
                    enter()

            elif (opcao == 2):

                # cidade de origem

                lista[0]= input ('\n ♦ Digite a nova cidade de origem: ')

                voos[num_m]= lista 

                print ('\n ✔ Alteração feita com sucesso!')
                enter()

            elif (opcao == 3):

                # cidade de destino

                lista[1]= input ('\n ♦ Digite a nova cidade de destino: ')

                voos[num_m]= lista

                print ('\n ✔ Alteração feita com sucesso!')
                enter()

            elif (opcao == 4):

                # tempo médio

                lista[2]= input ('\n ♦ Digite o novo tempo médio: ')

                voos[num_m]= lista

                print ('\n ✔ Alteração feita com sucesso!')
                enter()

            elif (opcao == 5):

                #areonave

                lista[3]= input ('\n ♦ Digite a nova aeronave que foi utilizada durante o voo: ')

                voos[num_m]= lista

                print ('\n ✔ Alteração feita com sucesso!')
                enter()

            elif (opcao == 6):

                # nomes das cidades das escalas

                cidades= lista[4]

                cid= input ('\n ♦ Digite um novo nome da cidade de escalas ("0" para terminar): ')
                while (cid != '0'):
                    cidades.append(cid)
                    cid= input ('\n ♦ Digite um novo nome da cidade de escalas ("0" para terminar): ')

                lista[4]= cidades

                voos[num_m]= lista

                print ('\n ✔ Alteração feita com sucesso!')
                enter()

    else:
        print('\n ツ Voo não cadastrado. \n')
        enter()

def listarVoo(voos, num_l):

    print("\nﾉ༼༎ຶ⁠ Listando Voo ⁠༎ຶ⁠༽ﾉ\n")

    flag= percorre(voos, num_l)

    if (flag):

        listaVoo= voos[num_l]

        print (f'\n » Número do Voo: {num_l}')
        print (f'» Cidade de origem: {listaVoo[0]}')
        print (f'» Cidade de destino: {listaVoo[1]}')
        print (f'» Tempo médio: {listaVoo[2]}')
        print (f'» Aeronave: {listaVoo[3]}')
        print (f'» Nomes das cidades das escalas: ', end='')
        cidades= listaVoo[4]
        for c in cidades:
            print (f' - {c}', end='')

    else:
        print('\n ツ Voo não cadastrado. \n')
        enter()

def listarvo(dic):
    print("\nﾉ༼༎ຶ⁠ Listando todos os Voos ⁠༎ຶ⁠༽ﾉ\n")
    for numero in dic.keys():
        print("Número do Voo:",numero)
        b=dic.get(numero)
        c=b[4]
        print("Cidade de Origem:",b[0])
        print("Cidade de Destino:",b[1])
        print("Tempo Médio de Viagem:",b[2])
        print("Aeronave:",b[3])
        print("Cidades das Escalas:",end=" ")
        for elemento in c:
            print(elemento,end=" - ")
        print("\n")

def excluirv(dic):
    print("\nﾉ༼༎ຶ⁠ Excluindo um Voo ⁠༎ຶ⁠༽ﾉ\n")
    num=int(input("Digite o Número do Voo:"))
    controle=False
    for numero in dic.keys():
        if numero == num:
            controle=True
            a=numero
    if controle == False:
        print("\nﾉ༼༎ຶ⁠ Elemento não Encontrado ⁠༎ຶ⁠༽ﾉ\n")
    else:
        del dic[a]
        print ('\n ✔ Exclusão feita com sucesso!')