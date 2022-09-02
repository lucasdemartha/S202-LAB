from db.pessoa import PessoaDAO
from helper.WriteAJson import writeAJson


pessoa = PessoaDAO()

#ADICIONAR UM LIVRO
pessoa.create(1,"A Dance with Dragons", "George R. R. Martin", 2011, 29.90)
pessoa.create(2,"A Storm of Swords", "George R. R. Martin", 2000, 27.90)
pessoa.create(3,"The Winds of Winter", "George R. R. Martin", 2005, 28.90)

#ALTERAR O PRECO DE UM LIVRO PELO ID
pessoa.update(1,32.30)

#DELETAR UM LIVRO PELO ID
pessoa.delete(1)

#LER TODOS OS DOCUMENTOS DA COLLECTION
writeAJson(pessoa.read(),"livros")
