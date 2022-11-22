from rich import print
import os

print("-=-=-=-=-=-=-=-=-=-=-")
print("Exercícos sobre listas")
print("-=-=-=-=-=-=-=-=-=-=-")


print("Digite um número para ser adicionado à lista, quando o número for menor que zero a lista se encerrará e passaremos para a próxima etapa")
listanova = []
contador = 0
n = 0

while n >= 0:
    n = int(input("Digite um número: "))
    listanova.append(n)

def ordenar(lista, reverso = False):
    
    nova_lista = []

    apoio = 0
    apoioIndice = 0
    
    while lista != []:

        for i, elemento_nl in enumerate(lista):
            if reverso:
                if i == 0:
                    apoio = elemento_nl
                    apoioIndice = i
                else:
                    if(elemento_nl<apoio):
                        apoio = elemento_nl
                        apoioIndice = i

            else:
                if(elemento_nl>apoio):
                    apoio = elemento_nl 
                    apoioIndice = i
        
        lista.pop(apoioIndice)
        nova_lista.append(apoio)

        apoio = 0
    
    del nova_lista[-1]
    
    return nova_lista

listanova = ordenar(listanova)

numero = 0

espaco = []
pilha = listanova

while numero >= 0:
    os.system("cls");
    print(f"Sua pilha: {listanova}")
    print(f"Espaço: {espaco}")
    print("O que você deseja fazer?")
    
    print("1 - Remover elemento da lista")
    print("2 - Adicionar elemento na lista")
    print("3 - Gerar relatório final")
    
    resp = int(input())
        
    if resp == 1:

        numero = int(input("Digite um número para ser removido da lista: "))
    
        indiceNumRemocao = 0
        passouItemNumero = False

        for i, item in enumerate(listanova):
            if item == numero:
                passouItemNumero = True
                indiceNumRemocao = i
                break

        if(passouItemNumero == False):
            input("Digite um número de dentro da lista...")
            continue

        
        cont = len(pilha) - 1

        while(cont != indiceNumRemocao):
            contador += 1
            print("Removendo..")
            print(f"Pilha: {pilha}")
            print(f"Espaço: {espaco}")
            apoio = pilha[-1]

            del pilha[-1]
            # contador++
            espaco.append(apoio)
            # contador++    
            cont -= 1
        
        # Removeu
        del pilha[indiceNumRemocao]

        # Recolocar os elementos na pilha

        tamanho_espaco = len(espaco)

        while len(espaco) != 0:
            contador += 1
            print("Realocando...")
            print(f"Pilha: {pilha}")
            print(f"Espaço: {espaco}")
            apoio = espaco[-1]
            pilha.append(apoio)
            del espaco[-1]

    elif resp == 2:
        posicao = int(input("Digite a posição do novo número: ")) - 1
        novoNumero = int(input("Digite o novo número: "))
        
        pilha = listanova
        espaco = []

        cont = len(pilha)

        while(cont != posicao):
            contador += 1
            apoio = pilha[-1]

            del pilha[-1]
            # contador++
            espaco.append(apoio)
            # contador++    
            cont -= 1
        
        
        # # Removeu
        pilha.append(novoNumero)
        
        while len(espaco) != 0:
            contador += 1
            print("Realocando...")
            print(f"Pilha: {pilha}")
            print(f"Espaço: {espaco}")
            apoio = espaco[-1]
            pilha.append(apoio)
            del espaco[-1]

        print(f"Pilha: {pilha}")
        print(f"Espaço: {espaco}")


    elif resp == 3:
        break

while(len(pilha) != 0):
    apoio = pilha[-1]
    espaco.append(apoio)
    del pilha[-1]
    contador += 1

print("-=Relatório Final=-")
print(f"Pilha: {pilha}")
print(f"Espaco: {espaco}")
print(f"Contador: {contador}")