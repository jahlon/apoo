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
            "7": self.calcular_transacciones_abastecimiento,
            "8": self.buscar_libro_mas_costoso,
            "9": self.buscar_libro_menos_costoso,
            "10": self.buscar_libro_mas_vendido,
            "11": self.salir
        }
    
    def mostrar_menu(self):
        print("""
        Menú de la Tienda de Libros

        1. Registrar libro
        2. Eliminar libro
        3. Buscar libro por título
        4. Buscar libro por isbn
        5. Abastecer ejemplares de un libro
        6. Vender ejemplares de un libro
        7. Calcular transacciones de abastecimiento de un libro
        8. Buscar el libro más costoso
        9. Buscar el libro menos costoso
        10. Buscar el libro más vendido
        11. Salir
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
