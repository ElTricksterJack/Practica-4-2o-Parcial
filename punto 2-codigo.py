print("\nRuvalcaba Valverde Mguel Angel_1212_3W")
print("---------------PUNTO 2---------------")
trad = {

}
L = 1 
#ya definimos valores, dcionao y L perfecto

#con este while vamos a haser que puedas lladir palabras ilimitadas todas la que tu corazon pida
while L > 0:
    e = input("Introduce una palabra en español: ").lower()#con el lower ago que detecte tanto mayusculas y minusculas, hasi no se confunde
    i = input("Introduce la traducción en inglés: ").lower()
    trad[e.strip()] = i.strip()#Nota: con el strip quitas todos los espacios hasi no pasa el error de que si escribes un espasio por axidente no te funsione la traducion
    L = int(input("0 para cerrar el diccionario y cualquier otro número para continuar: "))#1:21 ya me canse pero solo caputra y ya
    print("/------------/")

print("Diccionario creado:")
for x, y in trad.items():#el valor x, y se les da el pale de palabras y descrisiones, para que digan todos los objetos de la lista
    #muahahahhaha que malvado soy
    #el items debuelve los objetos mostrados en una lista
    print(f"{x} : {y}")
print("/------------/")

#captura como maestro pokemon la frase 1:17
fra = input("Introduce la frase en español que deseas traducir: ").lower()

tra = []#esta lista la usaremos como el conducto de nuestra tarducion
for p in fra.split():#con el split dividimos todo lo que tiene espasios
    #con esto separo todas las palabras de la frase y las ago valores independietes para la "traducion"    
    tra.append(trad.get(p, p))#con el get consultamos si hay palabras del dicionario dentro del codigo
#recuerden que con el append metemos elementos a la lista de tra,
# y esos elementosson las palabras de trad que estan pasando por revision

ft = " ".join(tra)#esta parte es crusial ya que el join "ordenara" o se podria desir que la junta la lista tra
#y tambien hay que recordar que hay que espesificar con que se ba a rellenar, y qui puse un espasio

print("--Traducion--")
print(ft)
#al final solo se muestra la traducion

print("-------------------------------------")
print("Resultado: se cumplio el objetivo pedido de la actividad el punto 2\n")
