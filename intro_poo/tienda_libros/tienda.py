from datetime import datetime
from typing import Union


class Transaccion:
    """
    Representa una transacción de venta o adquisición que se ha realizado sobre un libro.
    """

    VENTA = 1
    ABASTECIMIENTO = 2

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


class Libro:
    """
    Representa un libro de la tienda. Esta clase es responsable de abastecer y vender ejemplares
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

    def vender(self, cantidad) -> bool:
        """
        Vende una cantidad dada de ejemplares del libro. Si no hay esa cantidad, no se realiza la venta y el método retorna false
        """
        if self.cantidad_actual >= cantidad:
            self.cantidad_actual -= cantidad
            transaccion = Transaccion(Transaccion.VENTA, cantidad)
            self.transacciones.append(transaccion)
            return True
        else:
            return False

    def abastecer(self, cantidad):
        """
        Abastece ejemplares del libro
        """
        self.cantidad_actual += cantidad
        transaccion = Transaccion(Transaccion.ABASTECIMIENTO, cantidad)
        self.transacciones.append(transaccion)

    def __str__(self):
        return f"{self.titulo}\n" + \
                f"ISBN: {self.isbn}"


class TiendaDeLibros:
    """
    Representa la tienda que contiene todos los libros
    """

    def __init__(self) -> None:
        """
        Inicializa el objeto que representa la tienda, asignando 0 en la caja y con un
        catálogo vacío.
        """
        self.caja = 0
        self.catalogo = dict()
    
    def registrar_libro(self, titulo, isbn, precio_venta, precio_compra, cantidad_actual):
        """
        Añade un nuevo libro al catálogo a partir de los parámetros recibidos. Si el libro
        ya está en el catálogo, el método no hace nada.
        """
        if self.buscar_libro_por_isbn(isbn) is None:
            libro = Libro(isbn, titulo, precio_venta, precio_compra, cantidad_actual)
            self.catalogo[isbn] = libro

    def buscar_libro_por_isbn(self, isbn) -> Union[Libro, None]:
        """
        Localiza un libro del catálogo dado su ISBN. Si no lo encuentra retorna None.
        """
        if isbn in self.catalogo.keys():
            return self.catalogo[isbn]
        else:
            return None

    def buscar_libro_por_titulo(self, titulo) -> Union[Libro, None]:
        """
        Localiza un libro del catálogo dado su título. Si no lo encuentra retorna None.
        """
        for libro in self.catalogo.values():
            if libro.titulo == titulo:
                return libro
        
        return None

    def eliminar_libro(self, isbn) -> bool:
        """
        Elimina un libro del catálogo dado su ISBN. Si no lo encuentra retorna False.
        """
        if isbn in self.catalogo.keys():
            del self.catalogo[isbn]
            return True
        else:
            return False

    def abastecer(self, isbn, cantidad) -> bool:
        """
        Abastece ejemplares de un libro dado su ISBN, Si no puede abastecer los ejemplares
        del libro, retorna False.
        """
        libro = self.buscar_libro_por_isbn(isbn)
        if libro is not None:
            libro.abastecer(cantidad)
            return True
        else:
            return False

    def vender(self, isbn, cantidad, fecha) -> bool:
        """
        Vende ejemplares de un libro dado su ISBN. Si no puede vender los ejemplares del libro,
        retorna False.
        """
        libro = self.buscar_libro_por_isbn(isbn)
        if libro is not None:
            return libro.vender(cantidad)            
        else:
            return False

    def libro_mas_costoso(self) -> Union[Libro, None]:
        """
        Retorna el libro con el precio de venta mayor. Si no hay libros en el catálogo
        retorna None
        """
        if len(self.catalogo) > 0:
            return max(self.catalogo, key=lambda x: x.precio_venta)
        else:
            return None

    def libro_mas_economico(self) -> Union[Libro, None]:
        """
        Retorna el libro con el precio de venta menor. Si no hay libros en el catálogo
        retorna None.
        """
        if len(self.catalogo) > 0:
            return min(self.catalogo, key=lambda x: x.precio_venta)
        else:
            return None

    def libro_mas_vendido(self) -> Union[Libro, None]:
        """
        Retorna el libro del cual se han vendido más ejemplares. Si no hay libros en el
        catálogo retorna None.
        """
        pass

