# Banco de dados
# Esse projeto é para estudos
# Com esse mini projeto você poderá:
#	- criar um banco de dados
#	- adicionar/remover/atualizar o banco de dados https://sqlitebrowser.org/dl/

import sqlite3
import os
import sys

banco = sqlite3.connect("banco.db")
cursor = banco.cursor()

while True:
	os.system("clear")
	print("\033[1;32mBANCO DE DADOS\n\033[m")
	print("""
MENU:

[1] - Cadastrar pessoas
[2] - Remover cadastros
[3] - Atualizar dados
[4] - Fechar o banco e sair
		""")
	opcao = str(input("O que deseja: ")).strip()
	if opcao.isnumeric():
		opcao = int(opcao)
		if opcao == 1:
				cursor.execute("CREATE TABLE IF NOT EXISTS pessoas(nome text,idade integer,email text)")

				nome = str(input("Nome: "))
				idade = int(input("Idade: "))
				email = str(input("Email: "))
				try:
					cursor.execute("INSERT INTO pessoas VALUES('"+nome+"','"+str(idade)+"','"+email+"')")
					banco.commit()
				except Exception as error:
					print("Erro ao realizar cadastro! {}".format(error))
				else:
					print("Cadastro realizado com sucesso!")
		elif opcao == 2:
			deletar = str(input("Deletar pela idade: "))
			try:
				cursor.execute("DELETE from pessoas WHERE idade = {}".format(deletar))
				banco.commit()
			except Exception as erros:
				print(erros)
				sys.exit()
			else:
				print("Deletado!")
		elif opcao == 3:
			try:
				nome2 = str(input("Nome: "))
				idade = str(input("Idade: "))
				cursor.execute("UPDATE pessoas SET nome = '"+nome2+"' WHERE idade = '"+idade+"'")
				banco.commit()
			except:
				print("Erro ao fazer alteração no banco! Tente novamente")
			else:
				print("Alterado com sucesso")
		elif opcao == 4:
			banco.close()
			sys.exit()
