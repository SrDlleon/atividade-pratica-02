from consultas import (
    buscar_livros_por_titulo,
    listar_livros,
    listar_livros_disponiveis,
    listar_livros_por_autor,
)
from database import criar_banco, nova_sessao
from operacoes import devolver_livro, emprestar_livro
from seed import popular_banco


criar_banco()

with nova_sessao() as session:
    popular_banco(session)

    print("\nTodos os livros:")
    for livro in listar_livros(session):
        print(
            f'{livro["id"]} - {livro["titulo"]} | Autor: {livro["autor"]} | '
            f'Disponivel: {livro["disponivel"]}'
        )

    print("\nLivros disponíveis:")
    for livro in listar_livros_disponiveis(session):
        print(f"{livro.id} - {livro.titulo}")

    print("\nBusca por parte do título:")
    for livro in buscar_livros_por_titulo(session, "a"):
        print(f"{livro.id} - {livro.titulo}")

    print("\nLivros de um autor:")
    for livro in listar_livros_por_autor(session, "Machado de Assis"):
        print(f"{livro.id} - {livro.titulo}")

    print("\nEmprestando um livro:")
    print(emprestar_livro(session, 1))

    print("\nDevolvendo um livro:")
    print(devolver_livro(session, 2))
