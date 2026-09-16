"""Interface de terminal da calculadora.

Toda a entrada e saída de dados vive aqui. A lógica matemática está em
cálculo.py e o armazenamento em histórico.py.
"""

from rich.table import Table
from rich.console import Console

from calculo import OPERACOES, Operacao, validar_numero
from historico import Historico
from utils import formatar_numero, formatar_operacao, pausa

console = Console()
historico = Historico()

OPCAO_HISTORICO = '8'
OPCAO_LIMPAR_HISTORICO = '9'
OPCAO_SAIR = '0'

# Textos de interface: pertencem a esta camada, não ao módulo de cálculo.
PERGUNTAS: dict[str, list[str]] = {
    '1': ['Qual é o primeiro número?', 'E o segundo?'],
    '2': ['De qual número você quer subtrair?', 'Quanto você quer subtrair?'],
    '3': ['Qual é o primeiro número?', 'E o segundo?'],
    '4': ['Qual número você quer dividir?', 'E por qual número?'],
    '5': ['Qual é a base?', 'E o expoente?'],
    '6': ['De qual número você quer a raiz quadrada?'],
    '7': ['Quantos por cento você quer calcular?', 'De qual valor?'],
}


def validar_consistencia_operacoes() -> None:
    """Garante que a quantidade de perguntas bate com a ariedade de cada operação.

    A ariedade em Operacao é a fonte da verdade sobre quantos números uma
    operação precisa. Essa checagem impede que PERGUNTAS fique dessincronizado
    dela -- por exemplo, ao adicionar uma operação nova e esquecer de ajustar
    um dos dois lugares.
    """
    for codigo, operacao in OPERACOES.items():
        quantidade_perguntas = len(PERGUNTAS[codigo])
        if quantidade_perguntas != operacao.ariedade:
            raise AssertionError(
                f"Operação '{operacao.nome}' (código {codigo}) tem ariedade "
                f'{operacao.ariedade}, mas PERGUNTAS[{codigo!r}] tem '
                f'{quantidade_perguntas} pergunta(s).'
            )


validar_consistencia_operacoes()


def menu() -> None:
    """Exibe o menu principal da calculadora."""
    tabela = Table(title='Menu da Calculadora')

    tabela.add_column("Opção", justify="center", style='cyan')
    tabela.add_column("Operação", justify="center", style='green')

    for codigo, operacao in OPERACOES.items():
        tabela.add_row(codigo, operacao.nome)

    tabela.add_row(OPCAO_HISTORICO, 'Ver Histórico')
    tabela.add_row(OPCAO_LIMPAR_HISTORICO, 'Limpar Histórico')
    tabela.add_row(OPCAO_SAIR, 'Sair')

    console.print(tabela)


def pedir_numeros(perguntas: list[str]) -> tuple[float, ...]:
    """Faz uma pergunta por número necessário e devolve todos já validados."""
    numeros: list[float] = []

    for pergunta in perguntas:
        while True:
            try:
                numeros.append(validar_numero(input(f'{pergunta}: ')))
                break
            except ValueError as erro:
                console.print(f'[bold yellow]{erro}[/]')
    return tuple(numeros)


def executar_operacao(opcao: str) -> None:
    """Pede os números, executa a operação e trata o resultado ou o erro."""
    operacao: Operacao = OPERACOES[opcao]

    pausa()
    numeros = pedir_numeros(PERGUNTAS[opcao])

    try:
        resultado = operacao.funcao(*numeros)
    except (ZeroDivisionError, ValueError, OverflowError) as erro:
        console.print(f'[bold red]{erro}[/]')
        pausa()
        return

    operacao_str = formatar_operacao(operacao.simbolo, numeros)
    console.print(f'Resultado: {operacao_str} = {formatar_numero(resultado)}\n')

    historico.adicionar(operacao.simbolo, numeros, resultado)
    pausa()

def exibir_historico() -> None:
    """Mostra todas as operações da sessão."""
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
        resposta = input('\nTem certeza que quer apagar o histórico? (s/n): ')
        resposta = resposta.strip().lower()

        if resposta in ('s', 'sim'):
            return True
        if resposta in ('n', 'nao', 'não'):
            return False

        console.print('[red]Opção inválida! Digite novamente.[/]')


def loop_principal():
    """Controla o fluxo da aplicação."""
    console.print(('[blue]Vamos calcular[/]\n'))

    while True:
        pausa()
        menu()

        opcao = input(('Escolha uma opção: ')).strip()
        pausa()

        if opcao in OPERACOES:
            executar_operacao(opcao)

        elif opcao == OPCAO_HISTORICO:
            exibir_historico()
            pausa(0.5)

        elif opcao == OPCAO_LIMPAR_HISTORICO:
            if confirmar_limpeza():
                historico.limpar()
                console.print('[yellow]Histórico apagado com sucesso.[/]')
            else:
                console.print('[dim]Operação cancelada.[/]')
            pausa()

        elif opcao == OPCAO_SAIR:
            console.print('[red]Saindo do sistema.[/]')
            pausa()
            break

        else:
            console.print('[bold red]Opção inválida! Digite novamente.[/]')
            pausa()

def main() -> None:
    """Ponto de entrada: executa a calculadora e encerra com elegância."""
    try:
        loop_principal()
    except (KeyboardInterrupt, EOFError):
        console.print('\n[red]Encerrado pelo usuário.[/]')

if __name__ == '__main__':
    main()