from sqlalchemy import select

from models import Livro


def emprestar_livro(session, livro_id):
    """Marque um livro como indisponível."""
    livro = session.scalar(select(Livro).where(Livro.id == livro_id))

    if livro is None:
        return "Livro nao encontrado."

    if not livro.disponivel:
        return "Livro nao esta disponivel."

    livro.disponivel = False
    session.commit()
    return "Livro emprestado com sucesso."


def devolver_livro(session, livro_id):
    """Marque um livro como disponível."""
    livro = session.scalar(select(Livro).where(Livro.id == livro_id))

    if livro is None:
        return "Livro nao encontrado."

    if livro.disponivel:
        return "Livro ja esta disponivel."

    livro.disponivel = True
    session.commit()
    return "Livro devolvido com sucesso."
