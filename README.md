# Calculadora Python 🧮

Uma calculadora de terminal (CLI) feita em Python, com interface colorida usando a biblioteca [`rich`](https://github.com/Textualize/rich), histórico de operações agrupado por sessão e validação de entrada.

## Funcionalidades

- Operações básicas: soma, subtração, multiplicação e divisão
- Tratamento de divisão por zero
- Histórico de cálculos, agrupado por sessão (conjunto de números usados)
- Opção de continuar com os mesmos números, trocar de números ou encerrar o programa
- Interface em terminal com tabelas e cores (via `rich`)

## Como instalar

1. Clone o repositório:
   ```bash
   git clone https://github.com/TairaComassetto/Calculadora-Python.git
   cd Calculadora-Python
   ```

2. (Opcional, recomendado) Crie um ambiente virtual:
   ```bash
   python -m venv .venv
   .venv\Scripts\activate   # Windows
   source .venv/bin/activate  # Linux/Mac
   ```

3. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

## Como executar

```bash
python main.py
```

## Estrutura do projeto

```
├── main.py         # Fluxo principal e interface com o usuário
├── calculo.py      # Lógica das operações matemáticas
├── historico.py    # Armazenamento do histórico de cálculos
├── utils.py        # Funções auxiliares (formatação, pausas)
├── requirements.txt
└── README.md
```

## Exemplo de uso

```
Vamos calcular?

Digite os números iniciais
Digite um número: 10
Digite outro número: 5

Os números atuais são 10 e 5

┌────────────────────────┐
│    Menu da Calculadora  │
├─────────┬───────────────┤
│ Opção   │ Operação      │
├─────────┼───────────────┤
│ 1       │ Somar         │
│ 2       │ Subtrair      │
│ 3       │ Multiplicar   │
│ 4       │ Dividir       │
│ 5       │ Ver Histórico │
│ 6       │ Limpar        │
│ 7       │ Sair          │
└─────────┴───────────────┘

Escolha uma opção: 1
Resultado: 10 + 5 = 15
```

## Melhorias futuras

- [ ] Adicionar testes automatizados (`pytest`)
- [ ] Persistir histórico em arquivo (JSON) entre execuções
- [x] Refatorar histórico para evitar estado global
- [ ] Adicionar suporte a mais operações (potência, raiz, etc.)

## Licença

Este projeto está sob a licença MIT.
