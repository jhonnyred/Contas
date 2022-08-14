al = 0.0
cond = 0.0
ener = 0.0
inter = 0.0
cons = 0.0
mant = 0.0
dados = [al, cond, ener, inter, cons, mant]
#hist = open('Histórico.txt', 'r')
#dados = open('Dados.txt', 'r')
def escrever(arquivo, lista):
    cont = 0
    for valor in lista:
        arquivo.write(lista[cont])
        cont += 1
def extrair(arquivo, lista):
    cont = 0
    for line in arquivo:
        line = line.rstrip()
        L = int(line)
        lista[cont] = L
        cont += 1
    return lista
def defina(a, b):
    a = input('Qual valor para ' + b + ':')
    return a
def pula_linha(NLi):
    while NLi != 0:
        print('\n')
        NLi = NLi - 1
    pass
while True:
    #print(última linha do histórico com as listas ou dicionários)
    pula_linha(5)
    print('==============================================================')
    entr = input('\n(B) Boletos  || (N) Notas fiscais  ||  (H) Histórico \n ==>  ').upper()
    if entr == 'B':
        while True:
            pula_linha(20)
            print("\n(A) Aluguel:", al,"|| (C) Condominio:", cond, "|| (E)Energia:", ener, "|| (I)Internet:", inter, '||  (S) SALVAR  ||  (Q) SAIR')
            w = input("Qual valor deseja alterar? \n").upper()
            if w == 'A':
                al = defina(al, 'aluguel')
                dados[0] = al
            elif w == 'C':
                cond = defina(cond, 'condominio')
                dados[1] = cond
            elif w == 'E':
                ener = defina(ener, 'energia')
                dados[2] = ener
            elif w == 'I':
                inter = defina(inter, 'internet')
                dados[3] = inter
            elif w == 'S':
                file = open('dados.txt', 'w')
                cont = 0
                for valor in dados:
                    valor = str(dados[cont])
                    file.write(valor + '\n')
                    cont += 1
            elif w == 'Q':
                break
#    elif entr == "N":
#        t = input('(C) Registrar Consumo || (M) Registrar Mantimento').upper()
#        if t == 'C':
#        elif t == 'M': 
