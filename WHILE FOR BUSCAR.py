frase=input("frase: ")
l=input("letra para buscar su localizacion: ")
i=0
while i!=len(frase):
    if l!=frase[i]:
        print("no localizada", i)
        i+=1
        continue
    print("se encontro en la busqueda", i)
    break