# Atividade Prática 02 - Biblioteca Persistente

Complete os arquivos da base usando SQLAlchemy ORM.

## Como executar

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
pip install -r requirements.txt
python main.py
```

## Defesa escrita

Responda ao final:

1. Para que serve o campo `disponivel` em `Livro`?
2. Por que é necessário chamar `session.commit()` após emprestar ou devolver?
3. Em qual consulta você usa o relacionamento entre `Livro` e `Autor`?

### Respostas

1. O campo `disponivel` indica se o livro pode ser emprestado (`True`) ou se ja esta emprestado/indisponivel (`False`).
2. `session.commit()` grava as alteracoes no banco. Sem isso, a mudanca de status do livro fica apenas em memoria e nao persiste.
3. O relacionamento `Livro - Autor` e usado em `listar_livros(session)` (acesso a `livro.autor.nome`) e em `listar_livros_por_autor(session, nome_autor)` (consulta com `join`).
