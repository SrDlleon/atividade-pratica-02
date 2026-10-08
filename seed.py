from sqlalchemy import select

from models import Autor, Livro


def popular_banco(session):
    """Cadastre autores e livros iniciais para testar a aplicação."""
    if session.scalar(select(Autor.id)) is not None:
        return

    autor_machado = Autor(nome="Machado de Assis", pais="Brasil")
    session.add(autor_machado)

    outros_autores = [
        Autor(nome="Clarice Lispector", pais="Brasil"),
        Autor(nome="George Orwell", pais="Reino Unido"),
    ]
    session.add_all(outros_autores)

    livros = [
        Livro(titulo="Dom Casmurro", ano=1899, disponivel=True, autor=autor_machado),
        Livro(
            titulo="Memorias Postumas de Bras Cubas",
            ano=1881,
            disponivel=False,
            autor=autor_machado,
        ),
        Livro(titulo="Quincas Borba", ano=1891, disponivel=True, autor=autor_machado),
        Livro(
            titulo="A Hora da Estrela",
            ano=1977,
            disponivel=False,
            autor=outros_autores[0],
        ),
        Livro(titulo="1984", ano=1949, disponivel=True, autor=outros_autores[1]),
        Livro(titulo="A Revolucao dos Bichos", ano=1945, disponivel=False, autor=outros_autores[1]),
    ]
    session.add_all(livros)
    session.commit()
