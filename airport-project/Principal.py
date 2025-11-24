from Pilotos import*
from Voos import*
from Viagens import*
from Arquivo import*
from Relatorio import*

Pilotos={}
Voo={}
Viagem={}

opcao=0
while opcao != 5:
    print("\nﾉ༼༎ຶ⁠ Menu - Principal ⁠༎ຶ⁠༽ﾉ\n")
    print("1 - Submenu de Pilotos")
    print("2 - Submenu de Voos")
    print("3 - Submenu de Viagens")
    print("4 - Relatório")
    print("5 - Sair")
    opcao=int(input("Qual Opção Deseja Executar?:"))
    while (opcao < 1 or opcao > 5):
        print("Opção não aceita!")
        enter()
        opcao= int ( input ('Qual Opção Deseja Executar (1 a 5)') )
    if opcao == 1:
        mpiloto(Pilotos)
    elif opcao == 2:
        mvoos(Voo)
    elif opcao == 3:
        mviagem(Viagem,Voo,Pilotos)
    elif opcao == 4:
        mostrar(Viagem, Voo, Pilotos)
    

linhaArqP(Pilotos)
linhaArqVoo(Voo)
linhaArVi(Viagem)

