# Calculadora Python 🧮

Uma calculadora de terminal (CLI) feita em Python, com interface colorida usando a biblioteca [`rich`](https://github.com/Textualize/rich), histórico de operações e validação de entrada.

## Funcionalidades

- Operações: soma, subtração, multiplicação, divisão, potência, raiz quadrada e porcentagem
- Tratamento de erros (divisão por zero, raiz de número negativo, entrada inválida)
- Cada operação pergunta os números de forma específica, uma pergunta por vez (ex: "Qual é a base?", "E o expoente?")
- Histórico de todos os cálculos feitos na sessão
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

## Menu

| Opção | Operação          |
|-------|--------------------|
| 1     | Somar              |
| 2     | Subtrair           |
| 3     | Multiplicar        |
| 4     | Dividir            |
| 5     | Potência           |
| 6     | Raiz Quadrada      |
| 7     | Porcentagem        |
| 8     | Ver Histórico      |
| 9     | Limpar Histórico   |
| 0     | Sair               |

## Exemplo de uso

```
Vamos calcular?

Escolha uma opção: 1
Qual é o primeiro número? 10
E o segundo? 5
Resultado: 10 + 5 = 15

Escolha uma opção: 5
Qual é a base? 2
E o expoente? 3
Resultado: 2 ^ 3 = 8

Escolha uma opção: 6
De qual número você quer a raiz quadrada? 16
Resultado: √(16) = 4
```

## Melhorias futuras

- [ ] Adicionar testes automatizados (`pytest`)
- [ ] Persistir histórico em arquivo (JSON) entre execuções
- [x] Refatorar histórico para evitar estado global
- [x] Adicionar suporte a mais operações (potência, raiz, porcentagem)

## Licença

Este projeto está sob a licença MIT.
