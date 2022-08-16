al = 0.0
cond = 0.0
ener = 0.0
inter = 0.0
cons = 0.0
mant = 0.0
nome = ['Aluguel: ', ' Condomínio: ', ' Energia: ', ' Internet: ', ' Consumo: ', ' Mentimentos: ']
dados = [al, cond, ener, inter, cons, mant]
hist = open('historico.txt', 'r')
valo = open('dados.txt', 'r')
def last_line(arquivo):
    last = None
    for i in arquivo:
        last = i
    return last
def escrever(arquivo, lista):
    cont = 0
    for valor in lista:
        valor = str(lista[cont])
        arquivo.write(valor + '\n')
        cont += 1
def extrair(arquivo, lista):
    cont = 0
    for line in arquivo:
        line = line.rstrip()
        try:
            L = float(line)
        except:
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
last = last_line(hist)
dados = extrair(valo, dados)
while True:
    pula_linha(15)
    print(last)
    pula_linha(1)
    entr = input('\n(B) Boletos  ||  (N) Notas fiscais  ||  (H) Histórico || (Q) Sair \n ==>  ').upper()
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
                escrever(file, dados)
            elif w == 'Q':
                break
    elif entr == "N":
        while True:
            pula_linha(20)
            t = input('(C) Registrar Consumo || (M) Registrar Mantimento || (S) Salvar || (Q) Sair \n ==>  ').upper()
            if t == 'C':
                cons = defina(cons, 'consumo')
                dados[4] = cons
            elif t == 'M':
                mant = defina(mant, 'mantimentos')
                dados[5] = mant
            elif t == 'S':
                file = open('dados.txt', 'w')
                escrever(file, dados)
            elif t == 'Q':
                break
    elif entr == 'H':
        pula_linha(20)
        hist = open('historico.txt', 'r')
        for linha in hist:
            print(linha)
        pause = input() 
    elif entr == 'Q':
        file = open('historico.txt', 'a')
        cont = 0
        file.write('\n')
        for nom in nome:
            file.write(nom)
            dado = str(dados[cont])
            file.write(dado)
            cont += 1
        break 