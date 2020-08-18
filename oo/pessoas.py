class Pessoa:
    def __init__(self, *filhos, nome=None, idade = 57):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Olá {id(self)}' # imprimindo o id de self


if __name__ == '__main__':
    moacir = Pessoa(nome='Moacir')
    ricardo = Pessoa(moacir, nome='ricardo')
    # em class não precisa passar o atributo como parâmetro
    #vamos exemplificar com o id do objeto
    print(p.nome)
    print(Pessoa.cumprimentar(ricardo))
    print(id(ricardo))
    print(ricardo.cumprimentar())
    print(ricardo.nome)
#    p.nome = 'Ricardo'
#    print(p.nome)
    print(ricardo.idade)
    for filho in ricardo.filhos:
        print(filho.nome)



