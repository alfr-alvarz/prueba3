import json

def hacer_reporte(base_biblio):
    autores= []
    para_archivo = []
    for prestamo in base_biblio["Prestamo"]:

        prestamo["LibroID"]
        for libro in base_biblio["Libro"]:
            if libro["LibroID"] == prestamo["LibroID"]:
                autores.append(libro["AutorID"])
    
    print("""*********************************
*Autor\t\tCantidad de libros prestados
*************************************""")
    for autor in base_biblio["Autor"]:
        contador = 0
        for cantidad,autorid_iterado in enumerate(autores):
            if autor["AutorID"] == autorid_iterado:
                contador +=1
            if (cantidad+1) >= len(autores):
                print(autor["Nombre"],"\t",contador)
                para_archivo.append({autor["Nombre"]:contador})

    with open("Reportes_biblioteca_mundo_libro.json","w") as archivo_reporte:
        json.dump(para_archivo,archivo_reporte)
    