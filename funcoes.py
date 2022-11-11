from random import randint
posicoesInvalidas = ['E','A', 20]
especies = ["Ratata","Pidgey", "Weedle", "Caterpie", "Paras", "Charmander", "Bulbasaur", "Squirtle", "Pikachu","Evee"]
pokedex = []

def menu():
  print("Bem-vindo!\nA qualquer momento você pode escolher uma das opções:\n9 - Para abrir esse menu\n8 - Subir\n2- Descer\n4 - Ir para esquerda\n6 - Ir para direta\n5 - Abrir Pokedex\n0 - Sair do Jogo")
def menuPokedex():
  print("Digite\n1 para Listar Detalhes\n2 para Apagar Registro\n3 para ver tudo na pokedex\n0 para voltar ao menu principal")
def logicaDeMovimentacao(opcao,posicaoAtual,mapa):
    px = posicaoAtual['x']
    py = posicaoAtual['y']
    if(opcao == 8):
      if(mapa[px - 1][py] not in posicoesInvalidas):
        posicaoAtual["x"] -= 1 
      else :
        print("bump!")
    elif(opcao == 2):
      if(px + 1 <= 19  and mapa[px+1][py] != 'A' ): 
        posicaoAtual["x"] += 1
      else:
        print("bump!")  
    elif(opcao == 4):
      if(mapa[px][py - 1] not in posicoesInvalidas):
        posicaoAtual["y"] -= 1
      else :
        print("bump!")  
    else:
      if(mapa[px][py + 1] not in posicoesInvalidas):
        posicaoAtual["y"] += 1
      else :
        print("bump!")  
        
def aleatorio(valor):
    return randint(0,valor)

def pisouEmGrama(posicaoAtual,mapa):
  if(mapa[posicaoAtual['x']][posicaoAtual['y']] == 'G'):
    chance = aleatorio(1)
    if(chance == 1):
      print("Um pokemon selvagem apareceu!")
      capiturar = int(input("Capturar ou correr? [1-Capturar ou 2-Correr] "))
      if(capiturar == 1):
        salvaPokedex()
      else:
        print("fujão")

def salvaPokedex():
  novoPokemon = criaPokemon()
  print("apareceu um " + novoPokemon['especie'] )
  if(verifica(novoPokemon)):
    pokedex.append(novoPokemon)
    print("pokemon Capturado com sucesso")
  else:
    print("pokemon ja se encontra na pokedex")
    
def criaPokemon():
  pokemon = {}
  pokemon['especie'] = especies[aleatorio(9)]
  pokemon['HP'] = aleatorio(100)
  pokemon['Atk'] = aleatorio(100)
  pokemon['Def'] = aleatorio(100)
  pokemon['Sp'] = aleatorio(100) 
  return pokemon 

def verifica(novoPokemon):
  for i in pokedex:
    if(i['especie'] == novoPokemon['especie']):
      return 0
  return 1    
  
def procura(especie):
  for i in pokedex:
    if(i['especie'] == especie):
      print("seu "+ i["especie"]+ " tem as seguintes caracteristicas\nHP: " +str(i["HP"]) +"\nAtk: "+str(i['Atk']) + "\nDef: "+str(i['Def'])+ "\nSp: " + str(i['Sp'])+'\n')    

def deleta(especie):
  num = 0
  for i in pokedex:    
    if(i['especie'] == especie):
      pokedex.pop(num)       
    num += 1
    
def imprimePokedex():
  if(len(pokedex) > 0):
    for i in pokedex:
      print(i)
  else:
    print("capture um pokemon primeiro!!!\n")