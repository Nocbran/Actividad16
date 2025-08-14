from dis import code_info


class RegistoLibros:
    def __init__(self,codigounico,titulo,autor,añopublicado,):
        self.codigounico = codigounico
        self.titulo = titulo
        self.autor = autor
        self.añopublicado = añopublicado


        def MostrarInfo(self):
            return f"Codigo Unico: {self.codigounico} - Titulo: {self.titulo} - Autor: {self.autor} - Año Publicado: {self.añopublicado}"
class Usuarios:
    def __init__(self,carnet,nombre,carrera):
        self.carnet = carnet
        self.nombre = nombre
        self.carrera = carrera

        def MostarInf(self):
            return f"Carnet: {self.carnet} - Nombre: {self.nombre} - Carrera {self.carrera}"

class Gestiones:
    def __init__(self):
        self.libros = {}

    def AgregarLibros(self):
        try:
            codigo = int("Ingrese el codigo del libro: ")
            if codigo in self.libros:
                print("\nYa existe un libro registrado con ese codigo.")
                return
            titulo = input("Ingrese el titulo del libro: ")
            autor = input("Ingrese el autor: ")
            añio = int(input("Ingrese el año de publicacion: "))

            self.libros[codigo]

