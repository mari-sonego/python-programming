from datetime import datetime

def risco():
    print('\n ◠◠◠◠◠◠◠◠◠◠◠◠◠◠◠◠◠◠◠◠◠◠◠◠◠◠◠ \n')

def iguais(data, Viagens, Voos, Pilotos):

    listona= []

    for elem in Viagens:

        dataP= datetime.strptime(elem[2], '%d.%m.%Y')

        if dataP == data:

            n,p,d,h=elem
            q=Viagens[elem]

            for v in Voos:
                if v == n:
                    valor=Voos[v]
                    co=valor[0]
                    cd=valor[1]
            
            for pi in Pilotos:
                if p == pi:
                    val= Pilotos[pi]
                    nome=val[0]


            lista= [n,p,d,h,q,co,cd,nome]
            listona.append(lista)

    return listona

def diferentes(data1, data2, Viagens, Voos, Pilotos):

    listona=[]

    for elem in Viagens:

        dataP= datetime.strptime(elem[2], '%d.%m.%Y')

        if dataP < data1 and dataP > data2:

            n,p,d,h=elem
            q=Viagens[elem]

            for v in Voos:
                if v == n:
                    valor=Voos[v]
                    co=valor[0]
                    cd=valor[1]
            
            for pi in Pilotos:
                if p == pi:
                    val= Pilotos[pi]
                    nome=val[0]


            lista= [n,p,d,h,q,co,cd,nome]
            listona.append(lista)

    return listona

def mostrar(Viagens, Voos, Pilotos):
    d1 = input("\n ♦ Digite a primeira data (dd.mm.aaaa):")
    d2 = input(" ♦ Digite a segunda data (dd.mm.aaaa):")
    dt1 = datetime.strptime(d1, '%d.%m.%Y')
    dt2 = datetime.strptime(d2, '%d.%m.%Y')

    if dt2 > dt1:
        data2=dt1
        data1=dt2

        listona= diferentes(data1, data2, Viagens, Voos, Pilotos)

    elif dt1 > dt2:
        data1= dt1
        data2= dt2

        listona= diferentes(data1, data2, Viagens, Voos, Pilotos)

    else:
        listona = iguais(dt1, Viagens, Voos, Pilotos)


    if len(listona) == 0:
        print(" ツ Datas acima não condizentes com as viagens cadastradas. ")

    else:

        print('ﾉ༼༎ຶ⁠ Viagens cadastradas entre as datas acima: ⁠༎ຶ⁠༽ﾉ \n')

        for ele in listona:



            print("» Número do Voo: - ", ele[0])
            print("» Registro do Piloto: - ", ele[1])
            print("» Nome do piloto: - ", ele[7])
            print("» Cidade de origem: - ", ele[5])
            print("» Cidade de destino: - ", ele[6])
            print("» Data: - ", ele[2])
            print("» Hora: - ", ele[3])
            print("» Quantidade de passageiros: - ", ele[4])
            risco()


            




