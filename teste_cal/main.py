from rich.table import Table
from rich.console import Console
from rich import print
from calculo import somar, subtracao, multiplicacao, divisao, pedir_numeros
from time import sleep

console = Console()

def obter_numeros(mensagem):
    while True:
        try:
            sleep(1)
            return pedir_numeros(mensagem)
        except ValueError:
            print(f'[bold yellow]Digite apenas números.[/]')
            continue

def menu():
    tabela = Table(title='Menu da Calculadora')

    tabela.add_column("Opção", justify="center")
    tabela.add_column("Operação", justify="center")

    tabela.add_row('1', 'Somar',)
    tabela.add_row('2', 'Subtrair')
    tabela.add_row('3', 'Multiplicar')
    tabela.add_row('4','Dividir')
    tabela.add_row('5','Novos números')
    tabela.add_row('6', 'Sair')

    console.print(tabela)

n1, n2 = pedir_numeros('Digite os números iniciais')

while True:
    print(f'\nOs números atuais são {n1} e {n2}')
    menu()
    opcao = input('Escolha uma opção: ')
    if opcao == '6':
        console.print(f'[bold green]Fim do programa[/]')
        break
    elif opcao == '1':
        print(f'A soma entre {n1} + {n2} = {somar(n1, n2)}')
    elif opcao == '2':
        print(f'A subtração entre {n1} - {n2} = {subtracao(n1, n2)}')
    elif opcao == '3':
        print(f'A multiplicação entre {n1} x {n2} = {multiplicacao(n1, n2)}')
    elif opcao == '4':
        if n2 == 0:
            print('Não é possivel dividir por 0.')
        else:
            print(f'A divisão entre {n1} / {n2} = {divisao(n1, n2)}')
    elif opcao == '5':
        while True:
            try:
                sleep(1)
                n1, n2 = pedir_numeros('Digite os novos números')
                sleep(1)
                print(f'[bold green]Números atualizados...[/]\n')
                break
            except ValueError:
                print(f'[bold yellow]Digite apenas números.[/]')
    else:
        console.print(f'[bold red]Opção invalida! Digite novamente.[/]')
