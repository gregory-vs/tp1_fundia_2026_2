# Acompanhamento do TP1

## Concluído

- [x] Leitura e análise do enunciado.
- [x] Escolha do Python como linguagem de implementação.
- [x] Representação das pessoas e de seus tempos de travessia.
- [x] Representação de um estado por:
  - pessoas que permanecem no lado inicial;
  - lado em que a tocha se encontra.
- [x] Definição do estado inicial.
- [x] Definição do estado objetivo.
- [x] Função para verificar se um estado é objetivo.
- [x] Função para identificar as pessoas no lado final.
- [x] Função para calcular o custo de uma travessia.
- [x] Validação de travessias com uma ou duas pessoas.
- [x] Implementação da função sucessora.
- [x] Geração de movimentos de ida e de volta.
- [x] Criação do `main.py` como ponto de entrada do programa.
- [x] Exibição do estado inicial e de seus possíveis sucessores.
- [x] Criação do `README.md` com instruções de execução.
- [x] Verificação da sintaxe dos arquivos Python atuais.

## Implementação pendente

- [ ] Definir uma estrutura para os nós da busca, incluindo:
  - estado;
  - nó pai;
  - ação realizada;
  - custo acumulado;
  - profundidade.
- [ ] Implementar a reconstrução do caminho da solução.
- [ ] Implementar a Busca em Profundidade (DFS).
- [ ] Implementar a Busca em Largura (BFS).
- [ ] Implementar a Busca de Custo Uniforme ou Custo Mínimo (UCS).
- [ ] Propor e implementar uma heurística admissível.
- [ ] Justificar formalmente por que a heurística é admissível.
- [ ] Implementar a Busca A*.
- [ ] Adicionar um limite configurável de nós expandidos.
- [ ] Contabilizar os nós expandidos por cada algoritmo.
- [ ] Medir o tempo de processamento de cada execução.
- [ ] Exibir a sequência completa de travessias encontrada.
- [ ] Exibir o custo total da solução.
- [ ] Integrar os quatro algoritmos ao `main.py`.
- [ ] Permitir escolher qual algoritmo será executado.
- [ ] Tratar o caso em que o limite de nós é atingido sem solução.

## Testes e experimentos pendentes

- [ ] Criar testes automatizados para a representação dos estados.
- [ ] Criar testes automatizados para a função sucessora.
- [ ] Verificar se todos os movimentos gerados são válidos.
- [ ] Testar os quatro algoritmos separadamente.
- [ ] Verificar se UCS e A* encontram a solução ótima.
- [ ] Executar cada algoritmo várias vezes.
- [ ] Calcular os valores médios das métricas.
- [ ] Registrar, para cada algoritmo:
  - custo da solução;
  - número de nós expandidos;
  - tempo de processamento.
- [ ] Organizar os resultados em tabelas e, se conveniente, gráficos.

## Relatório pendente

- [ ] Criar a estrutura do relatório, preferencialmente em LaTeX.
- [ ] Escrever a introdução e a descrição do problema.
- [ ] Explicar a modelagem do problema como um grafo.
- [ ] Documentar a representação dos estados.
- [ ] Explicar as ações, transições, sucessores e custos.
- [ ] Explicar as principais rotinas implementadas.
- [ ] Apresentar os fundamentos de DFS, BFS, UCS e A*.
- [ ] Apresentar e justificar a função heurística.
- [ ] Descrever a metodologia dos experimentos.
- [ ] Comparar os resultados dos quatro algoritmos.
- [ ] Explicar por que BFS não garante a solução de menor tempo.
- [ ] Explicar por que UCS e A* garantem a solução ótima.
- [ ] Escrever a conclusão.
- [ ] Inserir e referenciar adequadamente tabelas, figuras e gráficos.
- [ ] Adicionar as referências bibliográficas em um padrão uniforme.
- [ ] Revisar clareza, gramática e formatação do relatório.

## Entrega

- [ ] Confirmar com os professores ou no Moodle o formato da entrega.
- [ ] Confirmar os arquivos que devem ser enviados.
- [ ] Conferir se o grupo possui exatamente quatro integrantes.
- [ ] Fazer uma execução final completa do projeto.
- [ ] Revisar o código e o relatório antes do envio.
