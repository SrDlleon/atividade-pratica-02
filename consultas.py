from sqlalchemy import select

from models import Autor, Livro


def listar_livros(session):
    """Liste todos os livros com o nome do autor e o status de disponibilidade."""
    livros = session.scalars(select(Livro)).all()
    return [
        {
            "id": livro.id,
            "titulo": livro.titulo,
            "autor": livro.autor.nome,
            "disponivel": livro.disponivel,
        }
        for livro in livros
    ]


def listar_livros_disponiveis(session):
    """Liste apenas os livros disponíveis."""
    livros = session.scalars(select(Livro).where(Livro.disponivel.is_(True))).all()
    return livros


def buscar_livros_por_titulo(session, trecho):
    """Busque livros por parte do título."""
    livros = session.scalars(select(Livro).where(Livro.titulo.ilike(f"%{trecho}%"))).all()
    return livros


def listar_livros_por_autor(session, nome_autor):
    """Liste os livros de um autor informado pelo nome."""
    livros = session.scalars(
        select(Livro).join(Livro.autor).where(Autor.nome == nome_autor)
    ).all()
    return livros
