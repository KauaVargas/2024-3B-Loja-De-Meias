import os

def mostra_titulo():

    print('𝓜𝓮𝓲𝓪𝓼 𝓗𝓸𝓪𝓱𝓲\n')

def mostra_escolhas():
    print('1. Cadastro de meias')
    print('2. Listar meias')
    print('3. Ativar meias')
    print ('4. Sair da aplicação')

def escolhe_opcao():
    opcao_escolhida = int(input('Escolha uma opção:'))
    print('Você escolheu a opção: ', opcao_escolhida)

    def finalizar_programa():
        os.system('cls')
        print('Finalizando programa')

    if opcao_escolhida == 1:
        print('Cadastrar meias')
    elif opcao_escolhida == 2:
        print('Listar meias')
    elif opcao_escolhida == 3:
        print('Ativar/Desativar meias')
    else:
        finalizar_programa()

def main():
    mostra_titulo()
    mostra_escolhas()
    escolhe_opcao()
    