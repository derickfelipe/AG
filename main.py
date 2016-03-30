#coding: utf-8
from functions import *
from os import system, name
clear = system('cls' if name == 'nt' else 'clear')

def ag(ind, tp, nger, tcross, tmut, tour, words):
    P = criar_pop_inicial_perm(ind, tp)
    print('Pop inicial\n', P)
    for i in range(nger):
        avaliar_pop(P, words)
        print(len(P), 'Pop avaliada\n', P)
        P.sort(key = lambda x: x[1], reverse = True) #insertion sort no avaliar_pop
        # pais = roleta(P, tcross)
        print(len(P), 'Pop avaliada, ordenada\n', P)
        pais = torneio(P, tour, tcross, tp)
        print(len(pais), 'Pais escolhidos\n', pais[:len(pais)//2], '\n', pais[len(pais)//2:])
        filhos = crossover_ciclico(pais, len(ind))
        #print(len(filhos), 'Filhos escolhidos\n', filhos)
        filhos = mutacao(filhos, tmut, len(ind))
        # print('Filhos mutados\n', filhos)
        filhos = avaliar_pop(filhos, words)
        print(len(filhos), 'Filhos avaliados\n', filhos)
        P = reinsercao_melhores_pf(P, filhos, tp)
        print(len(P), 'Reinsercao\n', P)
        if P[0][1] == 100000:
            break
    return P
        
def main():

    clear    
    ind = list(range(10))  
    tp = 10
    nger = 50
    tc = 60
    tm = 5
    exe = 1000
    # tp = 100
    # nger = 50
    # tc = 60
    # tm = 5
    # exe = 1
    tour = 2
    
    tcross = tc*tp//100
    tmut = tm*tp//100
    # print(tmut)
    words = ["send", 'more', 'money']
    R = []
    j = 0

    for i in range(exe):
        P = ag(ind, tp, nger, tcross, tmut, tour, words)
        print ('\n Execucao ', i, '   melhor individuo ', P[0][1])
        a = (i*100)/exe
        print ('\n', round(a, 2),'%')
        if (P[0][1] == 100000):
            j += 1
    
    print ('*********** CONVERGÊNCIA DE ' , j, '% EM ', i+1, 'EXECUÇÕES ***********')
    
    #test1 = [(7, 5, 1, 6, 0, 8, 9, 2, 3, 4), 0, 0]
    #test2 = [(6, 5, 7, 3, 4, 9, 1, 2, 8, 0), 0, 0]
    #t = [test1, test2]
    
    #print (t)

    #crossover_ciclico(t, 10)


    
    return        

main()
