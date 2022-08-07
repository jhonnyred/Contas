al = 0
cond = 0
ener = 0
inter = 0
despesas = []
while True:
	print("\n(A)Aluguel:", al,"(C)Condominio:", cond, "(E)Energia:", ener, "(I)Internet:", inter)
	w = input("Qual valor deseja alterar?(digite 'Q' para calcular)\n").upper()
	if w == "A":
		al = input("Digite um valor para o aluguel: ")
		despesas.append(al)
	elif w == "C":
		cond = input("Digite um valor para o condominio: ")
		despesas.append(cond)
	elif w == "E":
		ener = input("Digite um valor para a energia: ")
		despesas.append(ener)
	elif w == "I":
		inter = input("Digite um valor para a internet: ")
		despesas.append(inter)
	elif w == "Q":
		soma = float(al) + float(cond) + float(ener) + float(inter)
		print("\n Aluguel: ", al, "\n", "Condominio: ", cond, "\n", "Energia: ", ener, "\n", "Internet: ", inter, "\n")
		print("Soma das despesas: ", "%.2f"%soma)
		k = input("Deseja dividir a soma?(S/N) ").upper()
		if k == "S":
			k = input("Digite o número das partes a ser dividida: ")
			k = float(k)
			div = soma / k
			print("\n Total: ", "%.2f"%soma, "\n", "Para cada parte: ", "%.2f"%div)
			break
		elif k == "N":
			print("Total: ", "%.2f"%soma)
			break