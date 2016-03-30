#coding: utf-8
from random import randint, shuffle
from functools import reduce
from operator import add
from copy import copy

cap = 100000

def criar_pop_inicial_perm(ind, tp):
    '''Retorna P -> P[0] = 0, P[1] = ind, P[2] = 0'''
    P = set()
    i = 0
    while len(P) < tp and i < tp * 2:
        shuffle(ind)
        P.add(tuple(ind))
        i += 1
    if i >= tp*2:
        return print('Loop excedeu 2*tp')
    P = list(P)
    for i in range(len(P)):
        P[i] = [P[i], 0, 0]
    return P
    
def avaliar_pop(P, words):
    ''' recebe 3 palavras, soma as 2 primeiras e iguala à última'''
    base = len(P[0][0])
    temp = []
    for word in words:
        temp += word
    temp = set(temp)
    temp = list(temp)
    temp.sort()
    print ('\n\n', temp)
    for k in range(len(P)):
        n = [0 for x in words]
        for i in range(len(words)):
            for j in range(len(words[i])):
                index = temp.index(words[i][j])
                n[i] += P[k][0][index] * base ** abs(j - len(words[i])+1)
        P[k][1] = cap - abs((reduce(add, n[:-1]) - n[-1]))    
    return P
    
def res(P):
    for p in P:
        if p[1] == cap:
            return p[0]
    return 1
    
def res_ord(P):
    if P[0][1] == cap:
        return P[0]
    return 'Not found'
          
def roleta(P, tcross):
    ac = 0
    for i in range(len(P)):
        ac += P[i][1]
        P[i][2] = ac
    pais = []
    for i in range(tcross):
        p = randint(1, ac)
        for i in range(len(P)):
            if P[i][2] > p:
                pais.append(P[i][0])
                break
    return pais

def crossover_ciclico(pais, size):
    n = len(pais)
    if n % 2 != 0:
        pais.append(pais[0])
        n += 1
    n2 = n//2


    for i in range(n2):
        pai1 = list(pais[i][0])
        pai2 = list(pais[i+n2][0])
        pc = randint(0, size - 1)
        print ('\npc', pc)
        ciclo = copy(pc)
        print ('\npai1', pai1)
        temp = pai1[pc]
        pai2[pc] = pai1[pc]
        pai1[pc] = temp
        pc = pai1[pai1.index(pai1[pc])]
        
        while pc!= ciclo:
            temp = pai1[pc]
            pai2[pc] = pai1[pc]
            pai1[pc] = temp
            pc = pai1[pai1.index(pai1[pc])]
        print (pai1, pai2)
    
       
def mutacao(filhos, tmut, size):
    for i in range(tmut):
        r = randint(0, len(filhos)-1)
        r1 = randint(0, 7)
        r2 = randint(8, 9) 
        temp = list(filhos[r][0])
        temp2 = temp[r1]
        temp[r1] = temp[r2]
        temp[r2] = temp2
        filhos[r][0] = tuple(temp)
    return filhos
    
def torneio(L, tour, tcross, tpop):
    pais = []
    def escolhe_pai():
        temp = [0, 0]
        for i in range(tour):
            rand = randint(0, tpop-1)
            ava = L[rand][1]
            if ava > temp[1]:
                temp = [rand, ava]
        return L[rand]
    for j in range(tcross):
        pais.append(escolhe_pai())
    return pais
    
def reinsercao_melhores_pf(L, filhos, tp):
    L = (L + filhos)
    L.sort(key = lambda x: x[1], reverse = True)
    return L[:tp]