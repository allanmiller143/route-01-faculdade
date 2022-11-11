from mapa import *
from funcoes import *

posicaoAtual = {'x':19, 'y': 6}
opcao = -1

menu() 
print("\nEntrando na Rota 1")

while(opcao != 0 or (posicaoAtual['x'] == 0 and posicaoAtual['y'] == 6)): 
  print("Sua posição atual: " + str(posicaoAtual['x']) + " , " + str(posicaoAtual['y'])+"\n")
  opcao = int(input("escolha uma das opcoes a cima: "))  
  if(opcao == 9):
    mapa()
  elif(opcao == 8 or opcao == 2 or opcao == 4 or opcao == 6):
    logicaDeMovimentacao(opcao,posicaoAtual,mapa)
    pisouEmGrama(posicaoAtual,mapa)    
  elif(opcao == 5):
    menuPokedex()
    opcaoP = int(input("escolha umas das opcoes a cima: "))
    if(opcaoP == 1):
      especie = str(input("digite o nome da especie(primeira letra maiuscula) a ser procurada: "))
      procura(especie)
    elif(opcaoP == 2):
      especie = str(input("digite o nome da especie(primeira letra maiuscula) a ser retirada da pokedex: "))
      deleta(especie)
    elif(opcaoP == 3):
      imprimePokedex()
    elif(opcaoP == 0):
      print("de volta ao menu") 
    else:
      print("opcao invalida!!!")
        
  elif(opcao == 0):
    print("fim de jogo!")
    break
  else:
    print("opcao invalida, por favor tente novamente!")
  
  