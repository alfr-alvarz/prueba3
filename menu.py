import json
import os
import funciones
import reporte


with open("biblioteca.json","r") as archivobiblioteca:
    base_biblio = json.load(archivobiblioteca)
    while True:
        match input("""**********************************
*\t MUNDO LIBRO\t\t*
**********************************
[1] - Mantenedor de autores
[2] - Reportes
[3] - Salir
Opción: """):
            
            case "1":
                match input("""**********************************
*\tMANTENEDOR AUTORES\t*
**********************************
[1] - Agregar autor
[2] - Editar autor
[3] - Eliminar autor
[4] - Buscar autor
[5] - Volver
Opción: """):
                    case "1":
                        funciones.agregarautor(base_biblio)
                        input()
                        os.system("cls")

                    case "2":
                        funciones.editarautor(base_biblio)
                        input()
                        os.system("cls")
                    
                    case "3":
                        funciones.eliminarautor(base_biblio)
                        input()
                        os.system("cls")
                    
                    case "4":
                        funciones.busca_autor(base_biblio)
                        input()
                        os.system("cls")

                    case "5":
                        os.system("cls")
                        continue
            case "2":
                reporte.hacer_reporte(base_biblio)
                input()
            case "3":
                break
                

                