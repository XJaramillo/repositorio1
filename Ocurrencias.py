#Xavier Jaramillo Ocurrencia

def leertxt():
    archivo = open('Ocurrencia.txt', 'r')
    lineas = archivo.read()
    print(lineas)
    archivo.close()

    palabraslist = texto.split()
    Ocurrencia = []

    for a in palabraslist:
        Ocurrencia.append(palabraslist.count(a))

    lista = str(list(zip(palabraslist, Ocurrencia)))

    print(lista)
