import datetime

def read_file(arquivo):
    with open(arquivo, 'r') as file:
        items = file.readlines()
        return [i.strip('\n') for i in items]

arquivos = ['dataset-1-a.csv','dataset-1-b.csv', 'dataset-1-c.csv']

def encontra(n, D):
    start = datetime.datetime.now()
    for indice, item in enumerate(D):
        if item == n:
            final = datetime.datetime.now()
            time_stats = final - start
            return [True, indice, time_stats.microseconds]
    final = datetime.datetime.now()
    time_stats = final - start
    return [False, -1, time_stats.microseconds]

def result(arquivo):
    entrada = read_file(arquivo)
    resultado = encontra(entrada[0], entrada[2:])
    with open('resultado-'+arquivo+'.txt', 'w') as file:
        for i in resultado:
            file.write(str(i) + '\n')
        

for i in arquivos:
    result(i)


