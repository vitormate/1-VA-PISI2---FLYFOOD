def permutacoes(lista):
    #Casos base
    if len(lista) == 1:
        return [lista]
    if len(lista) == 0:
        return []
    lista_aux = []
    #Permutação Recursiva
    for i, elemento_atual in enumerate(lista):
        elementos_restantes = lista[:i] + lista[i+1:]
        for p in permutacoes(elementos_restantes):
            lista_aux.append([elemento_atual] + p)
    return lista_aux

def menor_percurso(lista, coordenadas):
    
    percurso_menor = []
    somatorio_menor = 0
    contador = 0

    for p in permutacoes(lista):

        contador += 1
        distancia = 0

        for i in range(len(p)):
                
                if i == 0:
                    distancia += abs(coordenadas['R'][0]-coordenadas[p[i]][0]) + abs(coordenadas['R'][1]-coordenadas[p[i]][1])
                elif i == (len(p)-1):
                    distancia += abs(coordenadas['R'][0]-coordenadas[p[i]][0]) + abs(coordenadas['R'][1]-coordenadas[p[i]][1])
                if i < (len(p)-1):
                    distancia += abs(coordenadas[p[i]][0]-coordenadas[p[i+1]][0]) + abs(coordenadas[p[i]][1]-coordenadas[p[i+1]][1])
        
        if contador == 1:
            percurso_menor = p
            somatorio_menor = distancia
        elif distancia < somatorio_menor:
            percurso_menor = p
            somatorio_menor = distancia
    
    return percurso_menor, somatorio_menor

def main():

    x = int(input("Digite o x do par ordenando do restaurante na matriz 4x5: "))
    y = int(input("Digite o y do par ordenando do restaurante na matriz 4x5: "))

    coordenadas = {'R': (x,y)}

    pontos = int(input("\nInforme a quantidade de pontos de entrega: "))

    lista = []

    alfabeto = 65

    for i in range(pontos):
        x = int(input(f"Digite o x do par ordenando do ponto de entrega {chr(alfabeto)} na matriz 4x5: "))
        y = int(input(f"Digite o y do par ordenando do ponto de entrega {chr(alfabeto)} na matriz 4x5: "))
        print()

        coordenadas[chr(alfabeto)] = (x,y)
        lista.append(chr(alfabeto))
        alfabeto += 1


    percurso_menor, somatorio_menor = menor_percurso(lista, coordenadas)

    print(f'O menor percurso é ', percurso_menor)
    print(f'A menor distância é: {somatorio_menor} quilômetros.')

main()