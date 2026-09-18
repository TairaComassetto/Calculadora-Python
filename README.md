# Calculadora Python 🧮

Uma calculadora de terminal (CLI) feita em Python, com interface colorida usando a biblioteca [`rich`](https://github.com/Textualize/rich), histórico de operações e validação de entrada.

## Funcionalidades

- Operações: soma, subtração, multiplicação, divisão, potência, raiz quadrada e porcentagem
- Tratamento de erros (divisão por zero, raiz de número negativo, entrada inválida, resultado fora de faixa)
- Cada operação pergunta os números de forma específica, uma pergunta por vez (ex: "Qual é a base?", "E o expoente?")
- Histórico de cálculos salvo automaticamente em disco, mantido entre execuções
- Interface em terminal com tabelas e cores (via `rich`)
- Encerramento tratado com Ctrl+C, sem exibir erros

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

## Como rodar os testes

```bash
pip install -r requirements-dev.txt
pytest -v
```

## Estrutura do projeto

```
├── main.py                    # Interface de terminal (toda a entrada e saída de dados)
├── calculo.py                 # Lógica matemática pura, sem entrada/saída
├── historico.py                # Armazenamento e persistência do histórico (JSON)
├── utils.py                   # Funções auxiliares (formatação, pausas)
├── historico.json              # Gerado automaticamente; não versionado (está no .gitignore)
├── tests/
│   ├── test_calculo.py        # Testes das operações e da validação
│   ├── test_historico.py      # Testes do histórico e da persistência em JSON
│   ├── test_utils.py          # Testes das funções de formatação
│   └── test_consistencia.py   # Garante que PERGUNTAS bate com a ariedade de cada operação
├── pytest.ini
├── requirements.txt
├── requirements-dev.txt       # Dependências extras para desenvolvimento (inclui pytest)
├── LICENSE
└── README.md
```

### Arquitetura

O projeto separa a lógica da interface. `calculo.py` não lê do teclado nem imprime na tela: recebe números, devolve números e levanta exceções. Quem cuida das perguntas, das mensagens e da apresentação é o `main.py`.

Essa separação facilita testar os cálculos sem simular entrada do usuário, e permite reaproveitar `calculo.py` e `historico.py` numa futura interface gráfica sem alteração alguma.

A persistência do histórico também fica dentro de `historico.py`: a classe `Historico` salva e carrega o `historico.json` sozinha, então qualquer interface que a use (terminal ou, futuramente, GUI) ganha isso automaticamente, sem precisar repetir a lógica de arquivo.

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

- [ ] Interface gráfica com Tkinter, reaproveitando a camada de cálculo
- [x] Separar a lógica de cálculo da interface de usuário
- [x] Refatorar histórico para evitar estado global
- [x] Adicionar suporte a mais operações (potência, raiz, porcentagem)
- [x] Adicionar testes automatizados (`pytest`)
- [x] Persistir histórico em arquivo (JSON) entre execuções

## Licença

Este projeto está sob a licença [MIT](LICENSE).
