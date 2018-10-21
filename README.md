# Substituição de Páginas
Neste projeto foi feito um programa
para simular o funcionamento dos principais
algoritmos de substituição de páginas. Código implementado em **Python 3.7**

Os algoritmos de substituição de páginas que
implementados são os seguintes:
* **FIFO (First In, First Out)**
* **OTM: Algoritmo Ótimo**
* **LRU: (Least Recently Used ou Menos Recentemente Utilizado)**

A entrada é composta por uma série números
inteiros, um por linha, indicando, primeiro a
quantidade de quadros disponíveis na memória
RAM e, em seguida, a sequência de referências à
memória. Caso queira alterar a entrada, 
mude no arquivo **instancias.txt**, por exemplo:

```
4
1
2
3
4
1
2
5
1
2
3
4
5
```

A saída do programa é composta por linhas contendo a sigla de cada
um dos três algoritmos e a quantidade de faltas de
página obtidas com a utilização de cada um deles, por exemplo:


```
FIFO 10
OTM 6
LRU 8
```

Para compilar apenas execute o comando no seu terminal:
>python substituicao_de_paginas.py 
