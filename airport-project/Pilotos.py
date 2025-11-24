from Arquivo import*

def mpiloto(Pilotos):

    existeArqP(Pilotos)
    
    menu=0
    while menu != 6:
        print("\nﾉ༼༎ຶ⁠ Menu - Piloto ⁠༎ຶ⁠༽ﾉ\n")
        print("1 - Listar Todos Os Pilotos")
        print("2 - Listar Um piloto")
        print("3 - Adicionar Um Piloto")
        print("4 - Alterar Um Piloto")
        print("5 - Excluir um Piloto")
        print("6 - Voltar\n")
        a=int(input("Qual Opção Deseja Executar?:"))
        if a == 1:
            listarp(Pilotos)
        elif a == 2:
            p=int(input("Digite o Registro do Piloto:"))
            listarPiloto(Pilotos,p)
        elif a == 3:
            incluirPiloto(Pilotos)
        elif a == 4:
            pp=int(input("Digite o Registro do Piloto:"))
            alterarPiloto(Pilotos,pp)
        elif a == 5:
            excluirp(Pilotos)
        elif a == 6:
            return
        else:
            print("\n ツ Opção Não Aceita!")
            enter()




def percorre(BD, igual):

    return (igual in BD)

def enter():

    input ('\n ﾉ༼༎ຶ⁠ Tecle <Enter> para continuar ༎ຶ⁠༽ﾉ')

def incluirPiloto(pilotos):

    print("\nﾉ༼༎ຶ⁠ Incluindo Piloto ⁠༎ຶ⁠༽ﾉ\n")

    rp= int ( input ('\n ♦ Digite o Registro do Piloto: ') )

    flag= percorre(pilotos, rp)

    if (flag):
        print('\n ツ Piloto já cadastrado anteriormente. \n')
        enter()

    else:

        nome= input ('\n ♦ Digite o nome do piloto: ')
        data= input ('\n ♦ Digite a data de nascimento do piloto: ')
        horas= input ('\n ♦ Digite as horas de voo do piloto: ') 
        email= input ('\n ♦ Digite o email do piloto: ')
        tel= input ('\n ♦ Digite o telefone do piloto: ')

        inf= [nome, data, horas, email, tel]

        pilotos[rp]= inf

        print('\n ✔ Piloto cadastrado com sucesso! \n')
        enter()

    return



def alterarPiloto(pilotos, rp_m):

    print("\nﾉ༼༎ຶ⁠ Alterando Piloto ⁠༎ຶ⁠༽ﾉ\n")

    flag= percorre(pilotos, rp_m)

    if (flag):

        opcao= 0

        while (opcao != 7):

            print ('\n ✸ Menu de Alterações ✸ \n')
            print ('1 ➸  Alterar o Registro do Piloto')
            print ('2 ➸  Alterar o nome do piloto')
            print ('3 ➸  Alterar a data de nascimento do piloto')
            print ('4 ➸  Alterar as horas de voo do piloto')
            print ('5 ➸  Alterar o email do piloto')
            print ('6 ➸  Alterar o telefone do piloto')
            print ('7 ➸  Finalizar alteramento')

            opcao= int ( input ('\n ♦ Digite a opção desejada: ') )

            while (opcao < 1 or opcao > 7):
                opcao= int ( input ('\n ♦ Número digitado fora do menu. Digite a opção desejada novamente: ') )

            lista= pilotos[rp_m]

            if (opcao == 1):

                #registro do piloto

                rp= int ( input ('\n ♦ Digite o novo Registro do Piloto: ') )

                tem= percorre(pilotos, rp)

                if (tem):
                    print ('\n » Registro de Piloto já existente!')
                    enter()

                else:

                    del pilotos[rp_m]

                    pilotos[rp]= lista

                    rp_m= rp

                    print ('\n ✔ Alteração feita com sucesso!')
                    enter()

            elif (opcao ==2):

                #nome

                lista[0]= input ('\n ♦ Digite o novo nome: ')

                pilotos[rp_m]= lista 

                print ('\n ✔ Alteração feita com sucesso!')
                enter()

            elif (opcao == 3):

                #data

                lista[1]= input ('\n ♦ Digite a nova data: ')

                pilotos[rp_m]= lista 

                print ('\n ✔ Alteração feita com sucesso!')
                enter()

            elif (opcao == 4):

                #horas de voo 

                lista[2]= input ('\n ♦ Digite a nova hora de voo: ')

                pilotos[rp_m]= lista 

                print ('\n ✔ Alteração feita com sucesso!')
                enter()

            elif (opcao == 5):

                #email

                lista[3]= input ('\n ♦ Digite o novo email: ')

                pilotos[rp_m]= lista 

                print ('\n ✔ Alteração feita com sucesso!')
                enter()

            elif (opcao == 6):

                #telefone

                lista[4]= input ('\n ♦ Digite o novo telefone: ')

                pilotos[rp_m]= lista 

                print ('\n ✔ Alteração feita com sucesso!')
                enter()

    else:
        print('\n ツ Piloto não cadastrado. \n')
        enter()

def listarPiloto(pilotos, rp_l):

    print("\nﾉ༼༎ຶ⁠ Listando Piloto ⁠༎ຶ⁠༽ﾉ\n")

    flag= percorre(pilotos, rp_l)

    if (flag):

        listaPiloto= pilotos[rp_l] 

        print (f'\n » Registro do Piloto: {rp_l}')
        print (f'» Nome: {listaPiloto[0]}')
        print (f'» Data de nascimento: {listaPiloto[1]}')
        print (f'» Horas de voo: {listaPiloto[2]}')
        print (f'» Email: {listaPiloto[3]}')
        print (f'» Telefone: {listaPiloto[4]} \n')
        enter()

    else:
        print('\n ツ Piloto não cadastrado. \n')
        enter()

def listarp(dic):

    print("\nﾉ༼༎ຶ⁠ Listando todos os Piloto ⁠༎ຶ⁠༽ﾉ\n")

    for nome in dic.keys():

        print("Registro do Piloto:",nome)

        a=dic.get(nome)
        
        print("Nome:",a[0])
        print("Data de Nascimento:",a[1])
        print("Horas de Voo:",a[2])
        print("E-mail:",a[3])
        print("Número de Telefone:",a[4],"\n")


def excluirp(dic):
    print("\nﾉ༼༎ຶ⁠ Excluindo um Piloto ⁠༎ຶ⁠༽ﾉ\n")

    nome=int(input("Digite o Registro do Piloto:"))
    controle=False

    for numero in dic.keys():

        if numero == nome:
            controle=True
            a=numero

    if controle == False:

        print("\nﾉ༼༎ຶ⁠ Elemento não Encontrado ⁠༎ຶ⁠༽ﾉ\n")

    else:

        del dic[a]
        print ('\n ✔ Exclusão feita com sucesso!')




