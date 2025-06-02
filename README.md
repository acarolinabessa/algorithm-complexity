# Análise de Complexidade de Algoritmos
Projeto apresentado para a disciplina de Análise e Projeto de Algoritmos que tem como objetivo analisar a **complexidade computacional** dos algoritmos de ordenação **Bubble Sort**, **Tree Sort** e **Shell Sort**, a partir da medição do **tempo de execução** e **uso de memória** em diferentes cenários: melhor caso, pior caso e casos médios.

## Objetivos
- Implementar os algoritmos de ordenação: **BubbleSort**, **TreeSort** e **ShellSort**;
- Executar os algoritmos com diferentes tamanhos de entrada (valores de `n`);
- Medir o tempo de execução (em segundos) e o uso de memória (em kB);
- Comparar os resultados de desempenho em diferentes casos;
- Gerar os resultados em um arquivo `.csv`.

## Funcionamento
Para cada valor de `n` e algoritmo escolhido, o programa executa três testes:

1. **Melhor caso:** dados em ordem crescente;
2. **Pior caso:** dados em ordem decrescente;
3. **Casos médios:** 5 execuções com dados organizados de forma aleatória, sendo o resultado a média de tempo e memória deles.


## Como executar
1. Clone o repositório
```bash
git clone https://github.com/acarolinabessa/algorithm-complexity.git
```
```bash
cd algorithm-complexity
```
2. Edite o arquivo `entrada.txt` com o valor de `n` e o algoritmo. Ex:
```bash
1000
bubblesort
```
3. Execute o programa
```bash
python main.py
```
4. Verifique os resultados em `resultados/resultados.csv`



