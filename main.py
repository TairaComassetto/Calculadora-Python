from rich.table import Table
from rich.console import Console
from calculo import pedir_numeros, Operacoes
from historico import adicionar, obter, limpar, nova_sessao
from utils import formatar_numero, pausa_curta, pausa_media, pausa_longa

console = Console()


def obter_numeros(mensagem):
    """Solicita dois números válidos ao usuário."""
    while True:
        try:
            pausa_media()
            console.print(mensagem)
            return pedir_numeros()
        except ValueError:
            console.print(f'[bold yellow]Digite apenas números.[/]')
            continue

def menu():
    """Exibe o menu principal da calculadora."""
    tabela = Table(title='Menu da Calculadora')

    tabela.add_column("Opção", justify="center", style='cyan')
    tabela.add_column("Operação", justify="center", style='green')

    tabela.add_row('1', 'Somar',)
    tabela.add_row('2', 'Subtrair')
    tabela.add_row('3', 'Multiplicar')
    tabela.add_row('4', 'Dividir')
    tabela.add_row('5', 'Ver Histórico')
    tabela.add_row('6', 'Limpar Histórico')
    tabela.add_row('7', 'Sair')


    console.print(tabela)

def exibir_historico():
    """Mostra todas as operações agrupadas por sessão."""
    hist = obter()
    if not hist:
        console.print('\n[yellow]Histórico vazio.[/]\n')
        return

    # Agrupa as operações que utilizaram os mesmos números.
    grupos = []
    for item in hist:
        # Caso a sessão já exista, adiciona a operação nela.
        if grupos and grupos[-1]['sessao'] == item['sessao']:
            grupos[-1]['itens'].append(item)
        else:
            grupos.append({
                'sessao': item['sessao'],
                'numeros': item['numeros'],
                'itens': [item]
            })

    for grupo in grupos:
        n1, n2 = grupo['numeros']
        # Cria uma tabela para cada sessão de cálculos.
        tabela = Table(
            title=f'[bold]Cálculos com {n1} e {n2}[/]',
            border_style='green'
        )
        tabela.add_column('#', justify='center', style='dim')
        tabela.add_column('Operação', justify='center')
        tabela.add_column('Resultado', justify='center', style='bold green')

        for i, item in enumerate(grupo['itens'], 1):
            tabela.add_row(str(i), item['operacao'], str(item['resultado']))

        console.print(tabela)
        console.print()


def confirmar_limpeza():
    """Pergunta ao usuário se deseja apagar o histórico."""
    while True:
        resposta = input('\nTem certeza que quer apagar o histórico? (s/n): ').strip().lower()
        if resposta in ('s', 'sim'):
            return True
        elif resposta in ('n', 'nao', 'não'):
            return False
        else:
            console.print('[red]Opção inválida! Digite novamente.[/]')

def menu_continuacao():
    """Exibe as opções após a realização de uma operação."""
    while True:
        tabela = Table(title='[bold]O que deseja fazer agora[/]')
        tabela.add_column('Opção', justify='center', style='green')
        tabela.add_column('Ação', justify='center', style='blue')

        tabela.add_row('1', 'Continuar com os mesmos números.')
        tabela.add_row('2', 'Continuar, MAS com novos números.')
        tabela.add_row('3', 'Encerrar programa.')

        console.print(tabela)

        pausa_media()
        escolha = input('Escolha um opção: ')

        if escolha in ['1', '2', '3']:
            return escolha

        console.print('Opção Inválida!')

def main():
    """Controla o fluxo principal da aplicação."""
    console.print('[blue]Vamos calcular?[/]\n')
    pausa_media()
    n1, n2 = obter_numeros('Digite os números iniciais')

    while True:
        console.print(f'\nOs números atuais são {formatar_numero(n1)} e {formatar_numero(n2)}\n')

        pausa_curta()
        menu()

        opcao = input('Escolha uma opção: ')

        pausa_media()
        if opcao in Operacoes:
            func, simbolo, simbolo_exibicao = Operacoes[opcao]
            resultado = func(n1, n2)

            if resultado is None:
                console.print('[red]Não é possível dividir por zero[/]')
                pausa_media()
                continue

            operacao = f'{formatar_numero(n1)} {simbolo} {formatar_numero(n2)}'
            console.print(f'Resultado: {formatar_numero(n1)} {simbolo_exibicao} {formatar_numero(n2)} = {formatar_numero(resultado)}\n')
            adicionar(operacao, formatar_numero(resultado), formatar_numero(n1), formatar_numero(n2))

        elif opcao == '5':
            exibir_historico()
            pausa_longa()
            continue

        elif opcao == '6':
            if confirmar_limpeza():
                limpar()
                console.print('\n[yellow]Histórico apagado com sucesso![/]\n')
            else:
                console.print('\n[dim]Operação cancelada.[/]\n')
                pausa_media()
                continue
        elif opcao == '7':
            console.print('[red]Saindo do sistema[/]')
            pausa_media()
            break
        else:
            console.print(f'[bold red]Opção invalida! Digite novamente.[/]')
            pausa_media()
            continue

        pausa_media()
        escolha = menu_continuacao()

        if escolha == '1':
            continue

        elif escolha == '2':
            nova_sessao()
            n1, n2 = obter_numeros('\nDigite os NOVOS números\n')
            pausa_media()
            console.print('\nNúmeros atualizados com sucesso!')
            pausa_media()

        elif escolha == '3':
            console.print('\nFIM DO PROGRAMA!')
            pausa_longa()
            break
if __name__ == '__main__':
    main()