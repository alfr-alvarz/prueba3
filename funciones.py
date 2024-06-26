import json

def agregarautor(base_biblio):
    nuevoautor = {
            "AutorID": None,
            "Nombre": input("Ingrese nombre del nuevo autor: "),
            "Nacionalidad": input("Ingrese su nacionalidad: ")
        }
    ids_existentes = []
    contador = 1
    for autor in base_biblio["Autor"]:
        ids_existentes.append(autor["AutorID"])
    
    while True:
        if contador in ids_existentes:
            contador += 1
        else:
            nuevoautor.update({"AutorID":contador})
            break
    base_biblio["Autor"].append(nuevoautor)
    print(nuevoautor)

    with open("biblioteca.json","w") as escribirbiblio:
        json.dump(base_biblio,escribirbiblio,indent=4)

def editarautor(base_biblio):
    id_buscada = int(input("Ingrese la ID del autor que modificará: "))
    indice_autor = None
    encontrado = False
    for indice,autor in enumerate(base_biblio["Autor"]):
        if autor["AutorID"] == id_buscada:
            indice_autor = indice
            encontrado = True
            break
    if not encontrado:
        print("No se ha encontrado la id.")
        return
    
    print("Ha elegido modificar:",base_biblio["Autor"][indice_autor])
    base_biblio["Autor"][indice_autor].update({"Nombre":input("Ingrese el nuevo nombre del Autor: "),"Nacionalidad":input("Ingrese la nueva nacionalidad: ")})

    with open("biblioteca.json","w") as escribirbiblio:
        json.dump(base_biblio,escribirbiblio,indent=4)

def eliminarautor(base_biblio):
    id_buscada = int(input("Ingrese la ID del autor que modificará: "))
    indice_autor = None
    encontrado = False
    for indice,autor in enumerate(base_biblio["Autor"]):
        if autor["AutorID"] == id_buscada:
            indice_autor = indice
            encontrado = True
            break
    if not encontrado:
        print("No se ha encontrado la id.")
        return
    
    print("Se eliminará:",base_biblio["Autor"][indice_autor])
    input()
    del base_biblio["Autor"][indice_autor]

    with open("biblioteca.json","w") as escribirbiblio:
        json.dump(base_biblio,escribirbiblio,indent=4)

def busca_autor(base_biblio):
    for autor in base_biblio["Autor"]:
        print(autor)