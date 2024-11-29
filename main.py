import json
import arrow
import time
import os

def main():
 global livros
 with open('livros.json', 'r', encoding='utf-8') as ficheiro_json:
    livros = json.load(ficheiro_json)
    menu()


def menu():
 while True:
  time.sleep(3)
  os.system("cls")
  option = 0
  print("1.Adicionar livros à biblioteca")
  print("2.Excluir livros")
  print("3.Listar livros")
  print("4.Requesitar")
  print("5.Devolver")
  print("6.Listar Requesitados ")
  option = input()
  if option == "1":
    print("nome do livro:")
    novo_titulo = input()
    print("nome autor:")
    autor=input()
    livros[novo_titulo] = {
    'autor': '',
    'status': '0'}
    livros[novo_titulo]['autor'] = autor
    autor = livros[novo_titulo]['autor']
    print(f"Título: {novo_titulo}")
    print(f"Autor: {autor}")
    print("Confirmar?Y/N")
    option = input()
    if option == "Y" or option == "y":
      with open('livros.json', 'w', encoding='utf-8') as ficheiro_json:
       json.dump(livros, ficheiro_json, ensure_ascii=False, indent=4)
      print("Livro adicionado!")
    elif option == "N" or option == "n":
      print("Processo terminado")
  elif option == "2":
        print("Livro a eliminar:")
        tituloaeliminar = input()
        if tituloaeliminar in livros:
            print(f"Tem a certeza que deseja eliminar o livro '{tituloaeliminar}'? Esta ação não pode ser revertida.")
            print("y/n")
            option = input()  
            if option == "Y" or option == "y":
                del livros[tituloaeliminar]  #
                with open('livros.json', 'w', encoding='utf-8') as ficheiro_json:
                    json.dump(livros, ficheiro_json, ensure_ascii=False, indent=4)  
                print(f"O livro '{tituloaeliminar}' foi eliminado com sucesso.")
            elif option == "N" or option == "n":
                print("Processo cancelado.")
        else :
           print("livro nao existe")
  elif option == "3":
     print("Livros:")
     for titulo, info in livros.items():
        print(f"Título: {titulo} - Autor: {info['autor']} - Status: {info['status']} - Data:{info['data']}")
     print("Enter to conclude")
     input()
  elif option == "4":
     print("Nome livro:")
     nomelivro = input()
     if livros[nomelivro]['status'] == "nr":
        livros[nomelivro]['data'] = arrow.now().format('YYYY-MM-DD')
        livros[nomelivro]['status'] = "r"
        with open('livros.json', 'w', encoding='utf-8') as ficheiro_json:
            json.dump(livros, ficheiro_json, ensure_ascii=False, indent=4)
        print(f"Livro{nomelivro}requesitado")  
     else:
        print("Livro não disponivel")
  elif option == "5":
     print("Nome livro:")
     nomelivro = input()
     livros[nomelivro]['data'] = ""
     livros[nomelivro]['status'] = "nr"
     with open('livros.json', 'w', encoding='utf-8') as ficheiro_json:
        json.dump(livros, ficheiro_json, ensure_ascii=False, indent=4) 
     print("Livro devolvido") 
  elif option == "6":
     print("Livros:")
     for titulo, info in livros.items():
        if livros[titulo]["status"] == "r":
            print(f"Título: {titulo} - Autor: {info['autor']} - Status: {info['status']} - Data:{info['data']}")
            print("Enter to conclude")
            input()
  elif option == "exit":
     False
main()