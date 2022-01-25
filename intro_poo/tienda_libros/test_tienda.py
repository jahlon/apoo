import pytest

from intro_poo.tienda_libros.tienda import Libro, TiendaDeLibros

@pytest.fixture
def tienda_vacia():
    """Retorna una instancia de la tienta vacía"""
    return TiendaDeLibros()

@pytest.fixture
def tienda_con_dos_libros():
    """Retorna una instancia de la clase TiendaDeLibros que contiene dos instancias de libro"""
    libro_1 = Libro("12345", "El principito", 35000, 25000, 10)
    libro_2 = Libro("98765", "Cien años de soledad", 50000, 40000, 8)
    tienda = TiendaDeLibros()
    tienda.catalogo[libro_1.isbn] = libro_1
    tienda.catalogo[libro_2.isbn] = libro_2
    return tienda

def test_tienda_registra_libro(tienda_vacia):
    tienda_vacia.registrar_libro("12345", "El principito", 35000, 25000, 10)
    assert len(tienda_vacia.catalogo) == 1

def test_buscar_libro_por_isbn(tienda_con_dos_libros):
    assert tienda_con_dos_libros.buscar_libro_por_isbn("12345") is not None

def test_buscar_libro_retorna_None_si_no_lo_encuentra(tienda_con_dos_libros):
    assert tienda_con_dos_libros.buscar_libro_por_isbn("11111") is None
    assert tienda_con_dos_libros.buscar_libro_por_titulo("El juego del angel") is None

def test_tienda_no_hace_nada_si_libro_existe(tienda_con_dos_libros):
     tienda_con_dos_libros.registrar_libro("El principito", "12345", 35000, 25000, 10)
     assert len(tienda_con_dos_libros.catalogo) == 2
    
def test_buscar_libro_por_titulo(tienda_con_dos_libros):
    assert tienda_con_dos_libros.buscar_libro_por_titulo("El principito") is not None

def test_tienda_elimina_libro_de_catalogo(tienda_con_dos_libros):
    assert tienda_con_dos_libros.eliminar_libro("98765") == True
    assert len(tienda_con_dos_libros.catalogo) == 1

def test_tienda_no_elimina_libro_de_catalogo_si_no_lo_encuentra(tienda_con_dos_libros):
    assert tienda_con_dos_libros.eliminar_libro("11111") == False
    assert len(tienda_con_dos_libros.catalogo) == 2

def test_tienda_abastece_libro(tienda_con_dos_libros):
    tienda_con_dos_libros.abastecer("12345", 5)
    assert tienda_con_dos_libros.catalogo["12345"].cantidad_actual == 15

def test_tienda_vende_unidades_libro(tienda_con_dos_libros):
    tienda_con_dos_libros.vender("98765", 2)
    assert tienda_con_dos_libros.catalogo["98765"].cantidad_actual == 6