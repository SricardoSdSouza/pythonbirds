class Pessoa:
    def __init__(self, nome=None, idade = 57):
        self.idade = idade
        self.nome = nome

    def cumprimentar(self):
        return f'Olá {id(self)}' # imprimindo o id de self


if __name__ == '__main__':
    p = Pessoa('Moacir')
    print(Pessoa.cumprimentar(p))
    # em class não precisa passar o atributo como parâmetro
    #vamos exemplificar com o id do objeto
    print(id(p))
    print(p.cumprimentar())
    print(p.nome)
    p.nome = 'Ricardo'
    print(p.nome)
    print(p.idade)



