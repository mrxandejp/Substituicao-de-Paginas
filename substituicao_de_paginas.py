



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
                        continue
                        pass
                    cont+=1
                    pass
                distante.append(cont)
                pass

            for y in range(len(referencia) - x):
                if y in distante:
                    ind = distante.index(y)
                    pass
                pass
            print(distante, ind)
            quadro[ind] = referencia[x]
            del distante
            pass
        #print(quadro)
        faltas_de_paginas+=1
        pass
    print("OTM:", faltas_de_paginas)    
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

FIFO(tamanho_quadro, referencia)
OTM(tamanho_quadro, referencia)
''' 
insertionSort()

fcfs()
sjf()
rr()
'''