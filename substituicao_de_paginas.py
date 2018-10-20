


def FIFO(tamanho_quadro, referencia):
    quadro = []
    faltas_de_paginas = 0
    chegada = []

    for x in range(len(referencia)):
        if referencia[x] in quadro:
            continue
            pass
        
        if len(quadro) < tamanho_quadro:
            quadro.append(referencia[x])
            chegada.append(referencia[x])
            pass
        else:
            i = quadro.index(chegada[0])
            del chegada[0]
            quadro[i] = referencia[x]
            chegada.append(referencia[x])
            pass  
        faltas_de_paginas+=1

        pass  
    print("FIFO:", faltas_de_paginas)
    pass


def OTM(tamanho_quadro, referencia):
    quadro = []
    faltas_de_paginas = 0
    ind = 0
    for x in range(len(referencia)):
        if referencia[x] in quadro:
            continue
            pass
        if len(quadro) < tamanho_quadro:
            quadro.append(referencia[x])
            pass
        else:
            distante = []
            for y in range(len(quadro)):
                cont = 0
                for i in range(x, len(referencia)):
                    if quadro[y] == referencia[i]:
                        distante.append(cont)
                        break
                        pass
                    cont+=1
                    pass
                if cont == (len(referencia) - x):
                    distante.append(1000)
                    pass
                pass
            ind = distante.index(max(distante, key=int))
            quadro[ind] = referencia[x]
            del distante
            pass
        faltas_de_paginas+=1
        pass
    print("OTM:", faltas_de_paginas)    
    pass

def LRU(tamanho_quadro, referencia):
    quadro = []
    faltas_de_paginas = 0
    contador = []

    for x in range(len(referencia)):
        if referencia[x] in quadro:
            ind = quadro.index(referencia[x])
            contador[ind] = 0
            pass
        else:    
            if len(quadro) < tamanho_quadro:
                quadro.append(referencia[x])
                contador.append(0)
                pass
            else:
                ind = contador.index(max(contador, key=int))
                quadro[ind] = referencia[x]
                contador[ind] = 0
                pass  
            faltas_de_paginas+=1
            pass        
        
        for y in range(len(contador)):
            contador[y] += 1
            pass
        pass 

    print("LRU:", faltas_de_paginas)
    pass

#Corpo principal
#Lendo o arquivo de instâncias para pegar os processos
ref_arquivo = open("instancias.txt","r")
tamanho_quadro = 0
referencia = []

for linha in ref_arquivo:
    referencia.append(int(linha))
ref_arquivo.close()

tamanho_quadro = referencia[0]
del referencia[0]
    
if tamanho_quadro == 0:
    print("FIFO: 0")
    print("OTM: 0")
    print("LRU: 0")
    pass 
else:    
    FIFO(tamanho_quadro, referencia)
    OTM(tamanho_quadro, referencia)
    LRU(tamanho_quadro, referencia)
    pass    
''' 
insertionSort()

fcfs()
sjf()
rr()
'''
'''
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
'''
'''
3
7
0
1
2
0
3
0
4
2
3
0
3
2
1
2
0
1
7
0
1
'''