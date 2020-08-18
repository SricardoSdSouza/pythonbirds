class Pessoa:
    olhos = 2
    def __init__(self, *filhos, nome=None, idade = 57):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Olá {id(self)}' # imprimindo o id de self

    @staticmethod
    def metodo_estatico():
        return 42

    @classmethod
    def nome_e_atributos_de_class(cls):
        return f'{cls} - olhos {cls.olhos}'

if __name__ == '__main__':
    moacir = Pessoa(nome='Moacir')
    ricardo = Pessoa(moacir, nome='ricardo')
    # em class não precisa passar o atributo como parâmetro
    #vamos exemplificar com o id do objeto
    print(Pessoa.cumprimentar(ricardo))
    print(id(ricardo))
    print(ricardo.cumprimentar())
    print(ricardo.nome)
#    p.nome = 'Ricardo'
#    print(p.nome)
    print(ricardo.idade)
    for filho in ricardo.filhos:
        print(filho.nome)
    # pode criar um atributo mesmo não estando no __init__
    ricardo.sobrenome = 'Souza'
    # pode deletar um atributo usando del
    #del ricardo.filhos
    ricardo.olhos = 1
    print(ricardo.sobrenome)
    print(ricardo.__dict__)
    print(moacir.__dict__)
    print(Pessoa.olhos)
    print(ricardo.olhos)
    print(moacir.olhos)
    print(id(Pessoa.olhos), id(ricardo.olhos), id(moacir.olhos))
    print(Pessoa.metodo_estatico(), ricardo.metodo_estatico())
    print(Pessoa.nome_e_atributos_de_class(), ricardo.nome_e_atributos_de_class())



