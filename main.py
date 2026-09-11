from os import system
import platform

def limpar_tela():
    if platform.system() == "Windows":
        system("cls")
    else:
        system("clear")

tarefas = []
inicio = str(input('INICIAR?\n'.rjust(14) + '\033[1;32mSim\033[m'.ljust(25) + '\033[1;31mNão\033[m\n'.rjust(14) + '\nDigite a opção escolhida: '))


while True:
    if inicio.lower() == 'sim':
        limpar_tela()


    opcao = int(input('\n\n\033[32m||Lista de Tarefas||\33[m\n\n[1] Adicionar Tarefa\n[2] Visualizar Tarefas\n[3] Concluir Tarefa\n[4] Remover Tarefa\n[5] Sair\n\nDigite a opção: '))


    if opcao == 1:

        print('Opção escolhida: Adicionar Tarefa...\n')
        new = input('Digite a nova Tarefa: ')
        tarefas.append(new)
        print('A Tarefa "{}" foi adicionada!\n'.format(new))

        new2 = input('Deseja adicionar mais uma tarefa? ')

        while new2.lower() == 'sim':
            new = input('\nDigite a nova Tarefa: ')
            tarefas.append(new)
            print('A Tarefa "{}" foi adicionada!\n'.format(new))
            new2 = input('Deseja adicionar mais uma tarefa? ')


    elif opcao == 2:
        print('Opção escolhida: Visualizar Tarefas...\n\n\033[34m||Lista de Tarefas||\33[m')

        if not tarefas:
            print('Nenhuma tarefa cadastrada!')
        else:
            for i in range(len(tarefas)):
                print(i + 1,'-', tarefas[i]), '\n'

            system('Pause')


    elif opcao == 3:
        print('Opção escolhida: Concluir Tarefas...\n\n\033[34m||Lista de Tarefas||\33[m')

        if not tarefas:
            print('Nenhuma tarefa cadastrada!')
        else:
            for i in range(len(tarefas)):
                print(i + 1, '-', tarefas[i])
            num = int(input('\nDigite o número da tarefa concluída: '))

            if num < 1 or num > len(tarefas):
                print('Número de tarefa inválido!')
            else:
                if tarefas[num - 1].startswith('✅'):
                    print('Essa tarefa já foi concluída!')
                else:
                    tarefas[num - 1] = '✅' + ' ' + tarefas[num - 1]

                    print('\n\033[34m||Lista de Tarefas||\33[m')
                    for i in range(len(tarefas)):
                        print(i + 1, '-', tarefas[i])

                    num2 = input('Deseja concluir mais uma tarefa? ')

                    while num2.lower() == 'sim':
                        num = int(input('Digite o número da tarefa concluída: '))

                        if num < 1 or num > len(tarefas):
                            print('Número de tarefa inválido!')

                        else:
                            if tarefas[num - 1].startswith('✅'):
                                print('Essa tarefa já foi concluída!')

                            else:
                                tarefas[num - 1] = '✅' + ' ' + tarefas[num - 1]

                                print('\n\033[34m||Lista de Tarefas||\33[m')

                                for i in range(len(tarefas)):

                                    print(i + 1, '-', tarefas[i])

                                num2 = input('Deseja concluir mais uma tarefa? ')


    elif opcao == 4:
        print('Opção escolhida: Remover Tarefa...\n\n\033[32m||Lista de Tarefas||\33[m')
        if not tarefas:
            print('Nenhuma tarefa cadastrada!')
        else:
            for i in range(len(tarefas)):
                print(i + 1, '-', tarefas[i])

            numero = int(input('\nDigite o número da tarefa que deseja remover: '))

            if numero < 1 or numero > len(tarefas):
                print('Número de tarefa inválido!')
            else:
                removida = tarefas.pop(numero - 1)

                print('\nA tarefa "{}" foi removida!\n'.format(removida))
                system('Pause')


    elif opcao == 5:
        print('Encerrando programa "Lista de Tarefas"...')
        break

