import os

meias = [{'nome':'12345', 'grupo de produtos':'masculino', 'estoque':True},
         {'nome':'23456', 'grupo de produtos':'feminino','estoque':True },
         {'nome':'34567', 'grupo de produtos':'infantil','estoque':True},
         {'nome':'45678', 'grupo de produtos':'cano alto','estoque':True}]


def exibir_subtitulo(texto):
    os.system('cls')
    print(texto)
    print('')

def retorna_menu_principal():
    input('\n Digite uma tecla para voltar ao menu principal')
    main()

def mostra_titulo():

    print('𝓜𝓮𝓲𝓪𝓼 𝓗𝓸𝓪𝓱𝓲\n')

def mostra_escolhas():
    print('1. Cadastro de meias')
    print('2. Listar meias')
    print('3. Ativar meias')
    print ('4. Sair da aplicação')

def escolhe_opcao():
    try:
        opcao_escolhida = int(input('Escolha uma opção:'))
        print('Você escolheu a opção: ', opcao_escolhida)

        if opcao_escolhida == 1:
            cadastrar_meias()
        elif opcao_escolhida == 2:
            mostrar_meias()
        elif opcao_escolhida == 3:
            print('Ativar/Desativar meias')
        elif opcao_escolhida == 4:
            finalizar_programa()   
        else:
            opcao_invalida()
    except:
        opcao_invalida()   

def cadastrar_meias():
    exibir_subtitulo('Cadastrar Meias')

    nome_meia = input('Digite o nome da meia: ')
    meias.append(nome_meia)
    print(f'{nome_meia} foi adicionado aos Itens')
    retorna_menu_principal()

def mostrar_meias():
    exibir_subtitulo('Listar Meias')

    for meia in meias:
        nome_meia = meia['nome']
        categoria = meia['grupo de produtos']
        ativo = meia['estoque']
        print(f' - {nome_meia} | {categoria} | {ativo}')

    retorna_menu_principal()

def finalizar_programa():
    os.system('cls')
    print('Finalizando programa')

def opcao_invalida():
    print('Esse caracter não é permitido')
    retorna_menu_principal()

def main():
    mostra_titulo()
    mostra_escolhas()
    escolhe_opcao()

if __name__ == '__main__':
    main()