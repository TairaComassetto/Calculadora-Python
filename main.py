from rich.table import Table
from rich.console import Console
from calculo import pedir_numeros, Operacoes
from historico import Historico
from utils import formatar_numero, pausa_curta, pausa_media, pausa_longa

console = Console()
historico = Historico()

opcao_historico = '8'
opcao_limpar_historico = '9'
opcao_sair = '0'

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
    func, perguntas, simbolo, simbolo_exibicao = Operacoes[opcao]

    numeros = obter_numeros_da_operacao(perguntas)
    resultado = func(*numeros)

    if resultado is None:
        console.print('[red]Operação inválida para esses valores (ex: divisão por zero ou raiz de número negativo).[/]')
        pausa_media()
        return

    numeros_fmt =[formatar_numero(n) for n in numeros]

    if len(numeros) == 1:
        operacao_str = f'{simbolo_exibicao}({numeros_fmt[0]})'
    else:
        operacao_str = f' {simbolo_exibicao} '.join(str(n) for n in numeros_fmt)

    console.print(f'Resultado: {operacao_str} = {formatar_numero(resultado)}\n')
    historico.adicionar(operacao_str, formatar_numero(resultado), tuple(numeros_fmt))
    pausa_media()


def exibir_historico() -> None:
    """Mostra todas as operações agrupadas por sessão."""
    hist = historico.obter()
    if not hist:
        console.print('\n[yellow]Histórico vazio.[/]\n')
        return

    tabela = Table(title='[bold]Histórico de Cálculos[/]', border_style='green')
    tabela.add_column('#', justify='center', style='dim')
    tabela.add_column('Operação', justify='center')
    tabela.add_column('Resultado', justify='center', style='bold green')

    for i, item in enumerate(hist, 1):
        tabela.add_row(str(i), item['operacao'], str(item['resultado']))

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

        if opcao in Operacoes:
            executar_operacao(opcao)

        elif opcao == opcao_historico:
            exibir_historico()
            pausa_longa()

        elif opcao == opcao_limpar_historico:
            if confirmar_limpeza():
                historico.limpar()
                console.print('[yellow]Histórico apagado com sucesso.[/]')
            else:
                console.print('[dim]Operação cancelada.[/]')
            pausa_media()

        elif opcao == opcao_sair:
            console.print('[red]Saindo do sistema.[/]')
            pausa_media()
            break

        else:
            console.print('[bold red]Opção inválida! Digite novamente.[/]')
            pausa_media()


if __name__ == '__main__':
    main()