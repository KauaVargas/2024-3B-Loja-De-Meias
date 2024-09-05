print('Meias Hoahi\n')

print('1. Cadastro de meias')
print('2. Listar meias')
print('3. Ativar meias')
print ('4. Sair da aplicação')

opcao_escolhida = int(input('Escolha uma opção:'))
print('Você escolheu a opção: ', opcao_escolhida)

if opcao_escolhida == 1:
    print('Cadastrar meias')
elif opcao_escolhida == 2:
    print('Listar meias')
elif opcao_escolhida == 3:
    print('Ativar/Desativar meias')
else:
    print('Saindo da aplicação')