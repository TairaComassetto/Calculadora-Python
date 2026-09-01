from rich.table import Table
from rich.console import Console
from calculo import pedir_numeros, OPERACOES
from historico import Historico
from utils import formatar_numero,formatar_operacao, pausa_curta, pausa_media, pausa_longa

console = Console()
historico = Historico()

OPCAO_HISTORICO = '8'
OPCAO_LIMPAR_HISTORICO = '9'
OPCAO_SAIR = '0'

def menu() -> None:
    """Exibe o menu principal da calculadora."""
    tabela = Table(title='Menu da Calculadora')

    tabela.add_column("Opção", justify="center", style='cyan')
    tabela.add_column("Operação", justify="center", style='green')

    tabela.add_row('1', 'Somar',)
    tabela.add_row('2', 'Subtrair')
    tabela.add_row('3', 'Multiplicar')
    tabela.add_row('4', 'Dividir')
    tabela.add_row('5', 'Potência')
    tabela.add_row('6', 'Raiz Quadrada')
    tabela.add_row('7', 'Porcentagem')
    tabela.add_row('8', 'Ver Histórico')
    tabela.add_row('9', 'Limpar Histórico')
    tabela.add_row('0', 'Sair')


    console.print(tabela)


def obter_numeros_da_operacao(perguntas: list[str]) -> tuple[float, ...]:
    """Solicita dois números válidos ao usuário."""
    while True:
        try:
            pausa_media()
            return pedir_numeros(perguntas)
        except ValueError as erro:
            console.print(f'[bold yellow]{erro}[/]')

def executar_operacao(opcao: str) -> None:
    """Pede os números certos, executa a operação e trata o resultado/erro."""
    func, perguntas, simbolo, simbolo_exibicao = OPERACOES[opcao]

    numeros = obter_numeros_da_operacao(perguntas)

    try:
        resultado = func(*numeros)
    except (ZeroDivisionError, ValueError) as erro:
        console.print(f'[bold red]{erro}[/]')
        pausa_media()
        return

    operacao_str = formatar_operacao(simbolo_exibicao, numeros)
    console.print(f'Resultado: {operacao_str} = {formatar_numero(resultado)}\n')

    historico.adicionar(simbolo_exibicao, numeros, resultado)
    pausa_media()

def exibir_historico() -> None:
    """Mostra todas as operações agrupadas por sessão."""
    hist = historico.obter()
    if not hist:
        console.print('\n[yellow]Histórico vazio.[/]\n')
        return

    tabela = Table(title='[bold]Histórico de Cálculos[/]', border_style='green')
    tabela.add_column('#', justify='center', style='dim')
    tabela.add_column('Operações', justify='center')
    tabela.add_column('Resultados', justify='center', style='bold green')

    for i, item in enumerate(hist, 1):
        operacao_str = formatar_operacao(item['simbolo'], item['numeros'])
        resultado_fmt = formatar_numero(item['resultado'])
        tabela.add_row(str(i), operacao_str, str(resultado_fmt))

    console.print(tabela)
    console.print()


def confirmar_limpeza() -> bool:
    """Pergunta ao usuário se deseja apagar o histórico."""
    while True:
        resposta = input('\nTem certeza que quer apagar o histórico? (s/n): ').strip().lower()
        if resposta in ('s', 'sim'):
            return True
        elif resposta in ('n', 'nao', 'não'):
            return False
        else:
            console.print('[red]Opção inválida! Digite novamente.[/]')


def main() -> None:
    """Controla o fluxo principal da aplicação."""
    console.print('[blue]Vamos calcular?[/]\n')

    while True:
        pausa_curta()
        menu()

        opcao = input('Escolha uma opção: ').strip()
        pausa_media()

        if opcao in OPERACOES:
            executar_operacao(opcao)

        elif opcao == OPCAO_HISTORICO:
            exibir_historico()
            pausa_longa()

        elif opcao == OPCAO_LIMPAR_HISTORICO:
            if confirmar_limpeza():
                historico.limpar()
                console.print('[yellow]Histórico apagado com sucesso.[/]')
            else:
                console.print('[dim]Operação cancelada.[/]')
            pausa_media()

        elif opcao == OPCAO_SAIR:
            console.print('[red]Saindo do sistema.[/]')
            pausa_media()
            break

        else:
            console.print('[bold red]Opção inválida! Digite novamente.[/]')
            pausa_media()


if __name__ == '__main__':
    main()