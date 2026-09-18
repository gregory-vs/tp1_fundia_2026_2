# TP1 — Problema da Ponte e da Tocha

Implementação em Python do problema da Ponte e da Tocha para a disciplina de
Fundamentos de Inteligência Artificial.

## Requisitos

- Python 3.10 ou mais recente

Confira se o Python está instalado:

```bash
python3 --version
```

## Compilação

Python é uma linguagem interpretada, portanto não é necessário compilar o
projeto para executá-lo. Para verificar a sintaxe do arquivo atual, use:

```bash
python3 -m py_compile estado.py
```

Se o comando terminar sem exibir mensagens, o arquivo não possui erros de
sintaxe. Esse comando pode criar a pasta `__pycache__`, usada internamente pelo
Python.

## Execução

No estado atual do projeto, `estado.py` contém a representação dos estados e
funções auxiliares. Ele pode ser carregado com:

```bash
python3 -c "import estado; print(estado.ESTADO_INICIAL)"
```

Também é possível abrir o interpretador do Python e importar o módulo:

```bash
python3
```

Em seguida:

```python
import estado

print(estado.ESTADO_INICIAL)
print(estado.ESTADO_OBJETIVO)
print(estado.custo_travessia(("A", "D")))
print(estado.sucessores(estado.ESTADO_INICIAL))
```

Para sair do interpretador, use `exit()`.

Execute o programa principal com:

```bash
python3 main.py
```

Atualmente, ele apresenta o estado inicial e todas as travessias que podem ser
feitas a partir dele. Os algoritmos de busca ainda serão adicionados.

## Arquivos atuais

- `estado.py`: representação dos estados, tempos das pessoas, função sucessora
  e funções auxiliares.
- `main.py`: ponto de entrada que apresenta o estado inicial e seus sucessores.
- `_Fund_IA__TP1_Ponte_Tocha.pdf`: enunciado do trabalho.
