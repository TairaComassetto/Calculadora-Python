from rich import print
from rich.table import Table
from rich.console import Console
from calculo import somar, subtracao, multiplicacao, divisao, pedir_numeros
from time import sleep

console = Console()

def obter_numeros(mensagem):
    while True:
        try:
            sleep(1)
            console.print(mensagem)
            return pedir_numeros()
        except ValueError:
            console.print(f'[bold yellow]Digite apenas números.[/]')
            continue

def menu():
    tabela = Table(title='Menu da Calculadora')

    tabela.add_column("Opção", justify="center")
    tabela.add_column("Operação", justify="center")

    tabela.add_row('1', 'Somar',)
    tabela.add_row('2', 'Subtrair')
    tabela.add_row('3', 'Multiplicar')
    tabela.add_row('4','Dividir')

    console.print(tabela)

def menu_continuacao():
    while True:
        tabela = Table(title='O que deseja fazer agora')
        tabela.add_column('Opção', justify='center')
        tabela.add_column('Ação', justify='center')

        tabela.add_row('1', 'Continuar com os mesmos números.')
        tabela.add_row('2', 'Continuar MAS com novos números.')
        tabela.add_row('3', 'Encerrar programa.')

        console.print(tabela)

        sleep(1)
        escolha = input('Escolha um opção: ')

        if escolha in ['1', '2', '3']:
            return escolha

        console.print('Opção Inválida!')

def main():
    console.print('[blue]Vamos calcular?[/]\n')
    sleep(1)
    n1, n2 = obter_numeros('Digite os números iniciais')

    while True:
        console.print(f'\nOs números atuais são {n1} e {n2}\n')

        sleep(0.8)
        menu()

        opcao = input('Escolha uma opção: ')

        sleep(1)
        if opcao == '1':
            console.print(f'A soma entre {n1} + {n2} = {somar(n1, n2)}\n')
        elif opcao == '2':
            console.print(f'A subtração entre {n1} - {n2} = {subtracao(n1, n2)}\n')
        elif opcao == '3':
            console.print(f'A multiplicação entre {n1} x {n2} = {multiplicacao(n1, n2)}\n')
        elif opcao == '4':
            resultado = divisao(n1, n2)
            if resultado is None:
                console.print('Não é possível dividir por zero!')
            else:
                console.print(f'A divisão entre {n1} / {n2} = {resultado}\n')
        else:
            console.print(f'[bold red]Opção invalida! Digite novamente.[/]')
            sleep(1)
            continue

        sleep(1)
        escolha = menu_continuacao()

        if escolha == '1':
            continue

        elif escolha == '2':
            n1, n2 = obter_numeros('\nDigite os NOVOS números\n')
            sleep(1)
            console.print('\nNúmeros atualizados com sucesso!')
            sleep(1)

        elif escolha == '3':
            console.print('\nFIM DO PROGRAMA!')
            sleep(1.3)
            break
if __name__ == '__main__':
    main()