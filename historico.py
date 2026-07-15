from copy import deepcopy

# Lista responsável por armazenar todas as operações realizadas.
historico = []

# Identifica a sessão atual de cálculos.
sessao_atual = 1

def adicionar(operacao: str, resultado, n1, n2):
    """Adiciona uma operação ao histórico."""
    historico.append({'operacao': operacao, 'resultado': resultado, 'numeros': (n1, n2), 'sessao': sessao_atual})

def obter():
    """Retorna uma cópia do histórico."""
    return deepcopy(historico)

def limpar():
    """Remove todas as operações do histórico."""
    historico.clear()

def nova_sessao():
    """Inicia uma nova sessão de cálculos."""
    global sessao_atual
    sessao_atual += 1