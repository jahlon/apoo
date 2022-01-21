from datetime import datetime
from types import UnionType
from xmlrpc.client import Boolean


class Libro:
    """
    Representa un libro de la tienda. Esta clase es responsable de abstecer y vender ejemplares
    del libro, así como de registrar una transacción por cada abastecimiento o venta que realice
    el usuario.
    """

    def __init__(self, isbn, titulo, precio_venta, precio_compra, cantidad_actual) -> None:
        """
        Inicializa un objeto Libro con la información asociada.
        """
        self._isbn = isbn
        self._titulo = titulo
        self._precio_venta = precio_venta
        self._precio_compra = precio_compra
        self._cantidad_actual = cantidad_actual
        self.transacciones = list()
    
    @property
    def isbn(self):
        return self._isbn
    
    @property
    def titulo(self):
        return self._titulo
    
    @property
    def precio_venta(self):
        return self._precio_venta
    
    @property
    def precio_compra(self):
        return self._precio_compra

    @property
    def cantidad_actual(self):
        return self._cantidad_actual
    
    @cantidad_actual.setter
    def cantidad_actual(self, nueva_cantidad):
        if nueva_cantidad < 0:
            raise Exception("La cantidad de libros no puede ser negativa")
        
        self._cantidad_actual = nueva_cantidad

    def vender(self, cantidad, fecha):
        """
        Vende una cantidad dada de ejemplares del libro
        """
        pass

    def abastecer(self, cantidad, fecha):
        """
        Abastece ejemplares del libro
        """
        pass

    def __str__(self):
        return f"{self.titulo}\n" + \
                f"ISBN: {self.isbn}"


class Transaccion:
    """
    Representa una transacción de venta o adquisición que se ha realizado sobre un libro.
    """

    def __init__(self, tipo, cantidad) -> None:
        """
        Inicializa un objeto de la clase, indicando el tipo de transacción (venta o adquisición) y
        la cantidad de ejemplares involucrados en la transacción.
        """
        self._tipo = tipo
        self._cantidad = cantidad
        self._fecha = datetime.now()
    
    @property
    def tipo(self):
        return self._tipo
    
    @property
    def cantidad(self):
        return self._cantidad

    @property
    def fecha(self):
        return self._fecha


class TiendaDeLibros:
    """
    Representa la tienda que contiene todos los libros
    """

    def __init__(self) -> None:
        """
        Inicializa el objeto que representa la tienda, asignao 0 en la caja y con un
        catálogo vacío.
        """
        self.caja = 0
        self.catalogo = list()
    
    def registrar_libro(self, titulo, isbn, precio_venta, precio_compra):
        """
        Anade un nuevo libro al catálogo a partir de los parámetros recibidos. Si el libro
        ya está en el catálogo, el método no hace nada.
        """
        pass

    def buscar_libro_por_isbn(self, isbn) -> UnionType[Libro, None]:
        """
        Localiza un libro del catálogo dado su ISBN. Si no lo encuentra retorna None.
        """
        pass

    def buscar_libro_por_titulo(self, titulo) -> UnionType[Libro, None]:
        """
        Localiza un libro del catálogo dado su título. Si no lo encuentra retorna None.
        """
        pass

    def eliminar_libro(self, isbn) -> Boolean:
        """
        Elimina un libro del catálogo dado su ISBN. Si no lo encuentra retorna False.
        """
        pass

    def abastecer(self, isbn, cantidad, fecha) -> Boolean:
        """
        Abastece ejemplares de un libro dado si ISBN, Si no puede abastecer los ejemplares
        del libro, retorna False.
        """
        pass

    def vender(self, isbn, cantidad, fecha) -> Boolean:
        """
        Vende ejemplares de un libro dado su ISBN. Si no puede vender los ejemplares del libro,
        retorna False.
        """
        pass

    def libro_mas_costoso(self) -> UnionType[Libro, None]:
        """
        Retorna el libro con el precio de venta mayor. Si no hay libros en el catálogo
        retorna None
        """
        pass

    def libro_mas_economico(self) -> UnionType[Libro, None]:
        """
        Retorna el libro con el precio de venta menor. Si no hay libros en el catálogo
        retorna None.
        """
        pass

    def libro_mas_vendido(self) -> UnionType[Libro, None]:
        """
        Retorna el libro del cual se han vendido más ejemplares. Si no hay libros en el
        catálogo retorna None.
        """
        pass

