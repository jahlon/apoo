import datetime
import sys
from tienda import TiendaDeLibros

class Menu:
    """
    Muestra un menú en pantalla y responde a las opciones que seleccione el usuario
    """

    def __init__(self) -> None:
        self.tienda = TiendaDeLibros()
        self.opciones = {
            "1": self.registrar_libro,
            "2": self.eliminar_libro,
            "3": self.buscar_libro_por_titulo,
            "4": self.buscar_libro_por_isbn,
            "5": self.abastecer_ejemplares,
            "6": self.vender_ejemplares,
            "7": self.buscar_libro_mas_costoso,
            "8": self.buscar_libro_menos_costoso,
            "9": self.buscar_libro_mas_vendido,
            "0": self.salir
        }
    
    def mostrar_menu(self):
        print("""
        \n
        ====================================
        Menú de la Tienda de Libros\n
        1. Registrar libro
        2. Eliminar libro
        3. Buscar libro por título
        4. Buscar libro por isbn
        5. Abastecer ejemplares de un libro
        6. Vender ejemplares de un libro
        7. Buscar el libro más costoso
        8. Buscar el libro menos costoso
        9. Buscar el libro más vendido
        0. Salir
        ====================================
        """)
    
    def ejecutar(self):
        """
        Muestra el menú y responde a la selección del usuario
        """
        while True:
            self.mostrar_menu()
            opcion = input("Seleccion una opción: ")
            accion = self.opciones.get(opcion)
            if accion:
                accion()
            else:
                print(f"{opcion} no es una opción válida.")

    def registrar_libro(self):
        print(">>> REGISTRAR LIBRO")
        print("Ingrese la información del libro\n")
        isbn = input("ISBN: ")
        titulo = input("Titulo: ")
        precio_venta = float(input("Precio de venta: "))
        precio_compra = float(input("Precio de compra: "))
        cantidad_actual = int(input("Cantidad actual: "))
        self.tienda.registrar_libro(titulo, isbn, precio_venta, precio_compra, cantidad_actual)
    
    def eliminar_libro(self):
        print(">>> ELIMINAR LIBRO\n")
        
        isbn = input("ISBN: ")
        
        if not self.tienda.eliminar_libro(isbn):
            print(f"INFO: No se encontró un libro con el ISBN {isbn}.")
        else:
            print(f"INFO: El libro fue eliminado del catálogo.")
    
    def buscar_libro_por_titulo(self):
        print(">>> BUSCAR LIBRO POR TÍTULO\n")

        titulo = input("Título: ")

        libro = self.tienda.buscar_libro_por_titulo(titulo)
        if libro is not None:
            print(libro)
        else:
            print(f"No se encontró un libro con el título: {titulo}")
    
    def buscar_libro_por_isbn(self):
        print(">>> BUSCAR LIBRO POR ISBN\n")

        isbn = input("ISBN: ")

        libro = self.tienda.buscar_libro_por_isbn(isbn)
        if libro is not None:
            print(libro)
        else:
            print(f"No se encontró un libro con el ISBN: {isbn}")
    
    def abastecer_ejemplares(self):
        print(">>> ABASTECER EJEMPLARES DE UN LIBRO\n")

        isbn = input("ISBN: ")
        cantidad = int(input("Cantida de ejemplares: "))

        if self.tienda.abastecer(isbn, cantidad):
            print("INFO: El abastecimiento se registró adecuadamente")
        else:
            print(f"INFO: No existe un libro con el ISBN {isbn}, por lo cual no se pudo registrar el abastecimiento")
    
    def vender_ejemplares(self):
        print(">>> VENDER EJEMPLARES DE UN LIBRO\n")

        isbn = input("ISBN: ")
        cantidad = int(input("Cantida de ejemplares: "))

        if self.tienda.vender(isbn, cantidad):
            print("INFO: La venta se registró adecuadamente")
        else:
            print(f"INFO: No existe un libro con el ISBN {isbn}, por lo cual no se pudo registrar la venta")
    
    def buscar_libro_mas_costoso(self):
        print(">>> BUSCAR LIBRO MÁS COSTOSO\n")

        libro = self.tienda.libro_mas_costoso()
        if libro is not None:
            print(libro)
        else:
            print("INFO: Aún no hay libros en el catálogo")
    
    def buscar_libro_menos_costoso(self):
        print(">>> BUSCAR LIBRO MENOS COSTOSO\n")

        libro = self.tienda.libro_mas_economico()
        if libro is not None:
            print(libro)
        else:
            print("INFO: Aún no hay libros en el catálogo")
    
    def buscar_libro_mas_vendido(self):
        print(">>> BUSCAR LIBRO MÁS VENDIDO\n")

        libro = self.tienda.libro_mas_vendido()
        if libro is not None:
            print(libro)
        else:
            print("INFO: Aún no hay libros en el catálogo")
    
    def salir(self):
        print("\nGRACIAS POR USAR LA APLICACIÓN")
        sys.exit(0)


if __name__ == "__main__":
    Menu().ejecutar()
        
