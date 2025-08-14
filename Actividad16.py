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

